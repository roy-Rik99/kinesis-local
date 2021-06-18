import boto3
import json
from datetime import datetime
from uuid import uuid4
import pickle
import websocket


class KinesisPublisher:
    def __init__(self, client=None, mock_endpoint="http://localhost:4568", test:bool=False):
        if(test==False):
            print("Actual Kinesis Client")
            # self.client = boto3.client(service_name='kinesis')
        else:
            self.client = boto3.client(service_name='kinesis', endpoint_url=mock_endpoint)
    def publishinStream(self, stream_name:str, data):
        payload = {
			'data' : data,
			"timestamp" : str(datetime.utcnow()),
            'source_type' : stream_name
			}
        resp = self.client.put_record(StreamName=stream_name, Data=json.dumps(payload), PartitionKey=str(uuid4()))
        print(resp)
    def publishfromFile(self, streamName="file-stream",filePath='files/filesource'):
        filehandler = open(filePath, 'rb')
        data=pickle.load(filehandler)
        print(data)
        for keys in data:
            self.publishinStream(stream_name=streamName,data=data[keys])
    def publishMessFromWB(self, wsapp, message):
        data=json.loads(message)
        print("\n\nPublished message to kinesis-->\n",data)
        self.publishinStream(stream_name="web-sockets",data=data)
    def get_data_WebSock(self, host):
        websocket.WebSocketApp(host, on_message=self.publishMessFromWB).run_forever()