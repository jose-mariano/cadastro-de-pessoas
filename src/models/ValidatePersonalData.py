class ValidatePersonalData:
	def isValidGender(self, gender):
		genders = ['masculino', 'feminino']

		if (gender in genders):
			return True

		return False


	def isValidName(self, name):
		nameLength = len(name)
		
		if ((nameLength == 0) or (nameLength < 3)):
			return False

		return True


