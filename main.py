import time
from utils.util_kinesis import KinesisUtil
from utils.util_generator import DataGenerator
from utils.util_publisher import KinesisPublisher


def kinesis_op():
	localstackURL="http://localhost:4568"
	kinesis_driver=KinesisUtil(mock_endpoint=localstackURL,test=True)
	streamName = str(input("\n\tEnter Stream Name? "))
	while True:
		print("\n\n\t1. CREATE Stream.\n")
		print("\t2. PRINT Data from Stream.(Use CTRL+C to terminate)\n")
		print("\t3. DELETE Stream.\n")
		print("\t4. EXIT.\n")
		op = int(input("\n\t\tEnter OPERATION?(1-5) "))
		if op == 1:
			kinesis_driver.createStream(stream_name=streamName, shard=1)
			time.sleep(10)
		elif op == 2:
			kinesis_driver.printRecords(stream_name=streamName)
		elif op == 3:
			kinesis_driver.deleteStream(stream_name=streamName, flag=True)
			time.sleep(10)
		elif op == 4:
			print("\n\tEXITING...\n\tBYE...")		
			break
		else:
			print("WRONG OPERATION")

if __name__ == "__main__":
	localstackURL="http://localhost:4568"
	publisher=KinesisPublisher(mock_endpoint=localstackURL,test=True)
	gen_data=DataGenerator()
	while True:
		print("\n\n")
		print("1. Generate and Publish demo data.","\n")
		print("2. Generate and Publish from File Sources.","\n")
		print("3. Publish messages from Web Sockets.(Use CTRL+C to terminate)","\n")
		print("4. Publish from IOT sensors.","\n")
		print("5. Perform Kinesis Operations.","\n")
		print("6. EXIT.","\n")
		op = int(input("\n\tEnter OPERATION?(1-6) "))
		if op == 1:
			i=0
			while i<10:
				person=gen_data.generatePerson()
				publisher.publishinStream(stream_name="demo", data=person)
				i+=1
		elif op == 2:
			gen_data.generateFile(filePath='files/filesource')
			publisher.publishfromFile(streamName="file-stream",filePath='files/filesource')
		elif op == 3:
			publisher.get_data_WebSock(host="wss://stream.meetup.com/2/rsvps")
		elif op == 4:
			print("Publish from IOT sensors","\n")
		elif op == 5:
			kinesis_op()
		elif op == 6:
			print("\n\tEXITING...\n\tBYE...")		
			break
		else:
			print("WRONG OPERATION")
