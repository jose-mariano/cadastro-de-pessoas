from src.repository import PeopleRepository
import re

class Person:
  _database = PeopleRepository()

  def __init__(self, data):
    dataKeys = data.keys()

    self.id = data['id'] if 'id' in dataKeys else None
    self.name = data['name'] if 'name' in dataKeys else ''
    self.birthDate = data['birthDate'] if 'birthDate' in dataKeys else ''
    self.gender = data['gender'] if 'gender' in dataKeys else ''
  
  @staticmethod
  def getPeople():
    try:
      people = Person._database.getPeople()

      return {
        'success': True,
        'data': people
      }
    except Exception as error:
      return {
        'success': False,
        'messages': [str(error)]
      }
  

  def create(self):
    try:
      self._checkName()
      self._checkBirthDate()
      self._checkGender()

      Person._database.create(self.name, self.birthDate, self.gender)
    
      return {'success': True}
    except Exception as error:
      return {
        'success': False,
        'messages': [str(error)]
      }


  def _checkGender(self):
    validGenders = ['masculino', 'feminino']

    if (self.gender.lower() not in validGenders):
      raise Exception('Gênero inválido! Gênero precisa ser "masculino" ou "feminino"!')
  

  def _checkName(self):
    nameLength = len(self.name)
    nameWithoutSpaces = self.name.replace(' ', '')

    if ((nameLength < 3) or (not nameWithoutSpaces.isalpha())):
      raise Exception('Nome inválido! Nome precisa conter no mínimo 3 letras!') 
  

  def _checkBirthDate(self):
    regex = r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$'

    if (not re.search(regex, self.birthDate)):
      raise Exception('Data inválida!')

