class ValidatePersonalData:
	def isValidGender(self, gender):
		genders = ['masculino', 'feminino']

		if (gender in genders):
			return True

		return False

