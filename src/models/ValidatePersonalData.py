from datetime import date

class ValidatePersonalData:
	def isValidGender(self, gender):
		genders = ['masculino', 'feminino']

		if (gender.lower() in genders):
			return True

		return False


	def isValidName(self, name):
		nameLength = len(name)
		nameWithoutSpaces = name.replace(' ', '')
		
		if ((nameLength < 3) or (not nameWithoutSpaces.isalpha())):
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


	def checkPersonalData(self, data):
		error = list()

		if (not self.isValidName(data['name'])):
			error.append('Nome inválido!')

		if (not self.isValidBirthDate(data['birthDate'])):
			error.append('Data de nascimento inválida!')

		if (not self.isValidGender(data['gender'])):
			error.append('Gênero inválido!')

		if (len(error) != 0):
			return {'erro': True, 'messages': error}

		return {'erro': False}
