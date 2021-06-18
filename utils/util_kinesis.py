import json, time, boto3



class KinesisUtil:
	def __init__(self, client=None, mock_endpoint="http://localhost:4568", test:bool=False):
		if(test==False):
			print("Actual Kinesis Client")
            # self.client = boto3.client(service_name='kinesis')
		else:
			self.client = boto3.client(service_name='kinesis',endpoint_url=mock_endpoint)
	def createStream(self, stream_name, shard):
		print("\n\tCREATING Stream "+stream_name+"......")
		response = self.client.create_stream(StreamName=stream_name, ShardCount=shard)
		print(response)

	def deleteStream(self, stream_name, flag):
		print("\n\tDELETING Stream "+stream_name+"......")
		response = self.client.delete_stream(StreamName=stream_name, EnforceConsumerDeletion=flag)
		print(response)
		
	def printRecords(self, stream_name):
		print("\n\tPRINTING Data from Stream "+stream_name+"......")
		response = self.client.describe_stream(StreamName=stream_name)
		shard_id = response['StreamDescription']['Shards'][0]['ShardId']
		shard_iterator_resp = self.client.get_shard_iterator(StreamName=stream_name,
                                                      ShardId=shard_id,
                                                      ShardIteratorType='LATEST')
		shard_iterator = shard_iterator_resp['ShardIterator']

		record_resp = self.client.get_records(ShardIterator=shard_iterator, Limit=2)
		
		while 'NextShardIterator' in record_resp:
			record_resp = self.client.get_records(ShardIterator=record_resp['NextShardIterator'], Limit=2)
			records=record_resp.get('Records')
			if(len(records)>0):
				data=json.loads(records[0].get('Data'))
				print(data,"\n\n")
			time.sleep(1)