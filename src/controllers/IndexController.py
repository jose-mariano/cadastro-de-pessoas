from src.views.CLI import CLI as Interface
from src.models.ValidatePersonalData import ValidatePersonalData
from src.models.PeopleDatabase import PeopleDatabase

class IndexController:
	def __init__(self):
		self.interface = Interface(self)
		self.validator = ValidatePersonalData()
		self.database = PeopleDatabase('people.sqlite3')


	def start(self):
		self.interface.start()


	def registerPerson(self, data):
		isValidData = self.validator.checkPersonalData(data)

		if (isValidData['erro']):
			return {'success': False, 'messages': isValidData['messages']}

		self.database.addPerson(data)

		return {'success': True}


	def getRegisteredPeople(self):
		return self.database.getPeople()




if __name__ == '__main__':
	IndexController().start()
