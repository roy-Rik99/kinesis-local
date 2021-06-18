
import random
import pickle

class DataGenerator:
	def __init__(self) -> None:
		pass
	def generatePerson(self):
		id = random.randint(1, 100000)
		name = "Person"+str(id)
		dob_year = random.randint(1967, 1999)
		dob_month = random.randint(1, 12)
		gender = random.choice(["Male", "Female"])
		salary = random.randint(40000, 2000000)
		person = {
			"Employee-ID":id,
			"Employee-Name":name,
			"DOB-Year":dob_year,
			"DOB-Month":dob_month,
			"Gender":gender,
			"Salary":salary}
		return person
	def generateFile(self,filePath='files/filesource'):
		filehandler = open(filePath, 'wb')
		data={}		
		for x in range(0, 200):
			data[x]=self.generatePerson()
		pickle.dump(data, filehandler)

		filehandler.close()