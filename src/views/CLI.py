class CLI:
	def __init__(self):
		self.data = dict()

	def getPersonData(self):
		self.data['name'] = str(input('Name: '))
		self.data['gender'] = str(input('Gender: '))
		self.data['birthDate'] = str(input('Birth date (DD-MM-YYYY): '))

		return self.data
