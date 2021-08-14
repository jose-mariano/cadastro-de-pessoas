from datetime import date

class ValidatePersonalData:
	def isValidGender(self, gender):
		genders = ['masculino', 'feminino']

		if (gender in genders):
			return True

		return False


	def isValidName(self, name):
		nameLength = len(name)
		
		if (nameLength < 3):
			return False

		return True


	def isValidBirthDate(self, birthDate):
		birthDateSplit = birthDate.split('-')

		if (len(birthDateSplit) != 3):
			return False

		try:
			year = int(birthDateSplit[0])
			month = int(birthDateSplit[1])
			day = int(birthDateSplit[2])

			date(year, month, day)
		except:
			return False

		return True
