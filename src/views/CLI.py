class CLI:
	def __init__(self, controller):
		self.controller = controller
		self.active = True
		self.options = [
			{
				'name': 'Ver pessoas cadastradas',
				'action': self.pageSeeRegisteredPeople
			},
			{
				'name': 'Cadastrar nova pessoa',
				'action': self.pageRegisterPerson
			},
			{
				'name': 'Sair',
				'action': self.exit
			}
		]


	def start(self):
		self.show('================= MENU =================', 'yellow')

		for index, item in enumerate(self.options):
			self.show(f"[{index + 1}] - {item['name']}", 'yellow')

		self.show('========================================', 'yellow')

		try:
			self.show('Opção: ', 'yellow', end="")
			userChoice = int(input()) - 1

			if (0 <= userChoice < len(self.options)):
				action = self.options[userChoice]['action']
				action()
			else:
				self.show('Escolha inválida, tente novamente!', 'red')
		except:
			self.show('Por favor, informe apenas números!', 'red')
		
		if (self.active):
			self.start()


	def pageRegisterPerson(self):
		data = dict()

		self.show('=========== CADASTRAR PESSOA ===========', 'yellow')
		self.show('Nome: ', 'yellow', end="")
		data['name'] = str(input()).strip()

		self.show('Dia de nascimento: ', 'yellow', end="")
		birthDay = str(input()).strip()
		self.show('Mês de nascimento: ', 'yellow', end="")
		birthMonth = str(input()).strip()
		self.show('Ano de nascimento: ', 'yellow', end="")
		birthYear = str(input()).strip()
		data['birthDate'] = f'{birthYear}-{birthMonth}-{birthDay}'

		self.show('Sexo(Masculino|Feminino): ', 'yellow', end="")
		data['gender'] = str(input()).strip().lower()
		self.show('========================================', 'yellow')

		result = self.controller.registerPerson(data)
		if (result['success']):
			self.show('Cadastro efetuado com sucesso!', 'green')
		else:
			for msg in result['messages']:
				self.show(msg, 'red')


	def pageSeeRegisteredPeople(self):
		people = self.controller.getRegisteredPeople()

		self.show('========= PESSOAS CADASTRADAS ==========', 'yellow')
		if (len(people) == 0):
			self.show('Não há pessoas cadastradas!', 'cyan')
		else:
			for person in people:
				name = person[0]
				birthYear, birthMonth, birthDay = person[1].split('-')
				gender = person[2]

				self.show('Nome: ', 'yellow', end="")
				self.show(name, 'cyan')
				self.show('Nascimento: ', 'yellow', end="")
				self.show(f'{birthDay}/{birthMonth}/{birthYear}', 'cyan')
				self.show('Sexo: ', 'yellow', end="")
				self.show(gender, 'cyan')
				self.show('----------------------------------------', 'yellow')


	def exit(self):
		self.active = False
		self.show('Sistema finalizado com sucesso!', 'green')


	def show(self, text, color='white', **kwargs):
		colors = {
			'white': '\033[1;97m',
			'black': '\033[1;30m',
			'red': '\033[1;31m',
			'green': '\033[1;32m',
			'yellow': '\033[1;33m',
			'blue': '\033[1;34m',
			'magenta': '\033[1;35m',
			'cyan': '\033[1;36m',
			'lightGray': '\033[1;37m',
			'darkGrey': '\033[1;90m',
			'lightRed': '\033[1;91m',
			'lightGreen': '\033[1;92m',
			'lightYellow': '\033[1;93m',
			'lightBlue': '\033[1;94m',
			'lightMagenta': '\033[1;95m',
			'lightCyan': '\033[1;96m'
		}
		reset = '\033[0;0m'

		print(f'{colors[color]}{text}{reset}', **kwargs)
