from src.views import getInterface
from src.models import Person

class IndexController:
	def __init__(self, interface):
		self.interface = getInterface(interface, self)


	def start(self):
		self.interface.start()


	def registerPerson(self, data):
		person = Person(data)
		
		return person.create()


	def getRegisteredPeople(self):
		return Person.getPeople()


