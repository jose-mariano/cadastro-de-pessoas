from src.views.CLI import CLI as Interface

class IndexController:
	def __init__(self):
		self.interface = Interface(self)
		self.interface.start()




if __name__ == '__main__':
	IndexController()
