from src.views.CLI import CLI as Interface
from src.models.ValidatePersonalData import ValidatePersonalData

class IndexController:
	def __init__(self):
		self.interface = Interface(self)
		self.validator = ValidatePersonalData()


	def start(self):
		self.interface.start()


	def registerPerson(self, data):
		isValidData = self.validator.checkPersonalData(data)

		if (isValidData['erro']):
			return {'success': False, 'messages': isValidData['messages']}

		return {'success': True}


	def getRegisteredPeople(self):
		return []




if __name__ == '__main__':
	IndexController().start()
