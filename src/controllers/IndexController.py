from src.views.CLI import CLI as Interface

class IndexController:
	def __init__(self):
		self.interface = Interface(self)
		self.interface.start()


	def registerPerson(self, data):
		print('\033[32;1mPessoa salva com sucesso!\033[m')


	def getRegisteredPeople(self):
		return []




if __name__ == '__main__':
	IndexController()
