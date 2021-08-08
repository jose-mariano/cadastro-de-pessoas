from src.views.CLI import CLI as Interface

class IndexController:
	def __init__(self):
		self.interface = Interface()

	def start(self):
		self.interface.getPersonData()




if __name__ == '__main__':
	IndexController().start()
