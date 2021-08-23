from src.views.CLI import CLI
from src.views.GUI import GUI
from src.models.ValidatePersonalData import ValidatePersonalData
from src.models.PeopleDatabase import PeopleDatabase

class IndexController:
	def __init__(self, interface):
		interfaces = {
			"CLI": CLI,
			"GUI": GUI
		}

		if (interface in interfaces.keys()):
			selectedInterface = interfaces[interface]
			self.interface = selectedInterface(self)
		else:
			raise "Enter which interface you want to use!"

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
