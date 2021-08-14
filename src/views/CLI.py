class CLI:
	def __init__(self, controller):
		self.controller = controller
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
		print('\033[33;1m================= MENU =================')

		for index, item in enumerate(self.options):
			print(f"[{index + 1}] - {item['name']}")

		print('========================================')

		try:
			userChoice = int(input('Opção: \033[m')) - 1

			if (0 <= userChoice < len(self.options)):
				action = self.options[userChoice]['action']
				action()
			else:
				print('\033[31;1mEscolha inválida, tente novamente!\033[m')
				self.start()

		except:
			print('\033[31;1mPor favor, informe apenas números!\033[m')
			self.start()


	def pageRegisterPerson(self):
		data = dict()

		print('\033[33;1m=========== CADASTRAR PESSOA ===========\033[m')

		data['name'] = str(input('\033[33;1mNome:\033[m ')).strip()
		birthDay = str(input('\033[33;1mDia de nascimento:\033[m ')).strip()
		birthMonth = str(input('\033[33;1mMês de nascimento:\033[m ')).strip()
		birthYear = str(input('\033[33;1mAno de nascimento:\033[m ')).strip()
		data['birthDate'] = f'{birthYear}-{birthMonth}-{birthDay}'
		data['gender'] = str(input('\033[33;1mSexo (masculino/feminino):\033[m ')).strip().lower()

		print('\033[33;1m========================================\033[m')

		self.controller.registerPerson(data)


	def pageSeeRegisteredPeople(self):
		people = self.controller.getRegisteredPeople()

		print('\033[33;1m========= PESSOAS CADASTRADAS ==========\033[m')

		if (len(people) == 0):
			print('Não há pessoas cadastradas!')
		else:
			for person in people:
				print(person)

		print('\033[33;1m========================================\033[m')


	def exit(self):
		print('\033[32;1mSistema finalizado com sucesso!\033[m')
