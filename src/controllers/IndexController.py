from src.views import getInterface
from src.models.ValidatePersonalData import ValidatePersonalData
from src.models.PeopleDatabase import PeopleDatabase

class IndexController:
	def __init__(self, interface=''):
		self.interface = getInterface(interface, self)
		self.validator = ValidatePersonalData()
		self.database = PeopleDatabase('people.sqlite3')


	def start(self):
		self.interface.start()


	def registerPerson(self, data):
		isValidData = self.validator.checkPersonalData(data)

		if (isValidData['erro']):
			return {'success': False, 'messages': isValidData['messages']}

		return self.database.addPerson(data)


	def getRegisteredPeople(self):
		return self.database.getPeople()




if __name__ == '__main__':
	IndexController('GUI').start()
