class CLI:
	def __init__(self, controller):
		self.data = dict()
		self.controller = controller
		self.options = [
			{
				'name': 'Ver pessoas cadastradas',
				'action': print
			},
			{
				'name': 'Cadastrar nova pessoa',
				'action': print
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

	def exit(self):
		print('\033[32;1mSistema finalizado com sucesso!\033[m')
