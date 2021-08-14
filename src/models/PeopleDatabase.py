import sqlite3 as database

class PeopleDatabase:
	def __init__(self, dbPath):
		self.db = database.connect(dbPath)
		self.cursor = self.db.cursor()

		self.__createTablePeople()


	def __createTablePeople(self):
		sql = """
			CREATE TABLE IF NOT EXISTS people(
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				name TEXT NOT NULL,
				birth_date TEXT NOT NULL,
				gender TEXT NOT NULL
			);
		"""

		self.cursor.execute(sql)


	def addPerson(self, personalData):
		data = (
			personalData['name'],
			personalData['birthDate'],
			personalData['gender'],
		)

		sql = """
			INSERT INTO people(name, birth_date, gender)
			VALUES (?,?,?);
		"""
		try:
			self.cursor.execute(sql, data)
			self.db.commit()

			return {"success": True}
		except:
			return {"success": False, "messages": ["Erro ao salvar pessoa no banco!"]}


	def getPeople(self):
		sql = """
			SELECT name, birth_date, gender FROM people
			ORDER BY name;
		"""

		try:
			self.cursor.execute(sql)
			result = self.cursor.fetchall()
			
			return {"success": True, "data": result}
		except:
			return {"success": False, "messages": ["Erro ao selecionar as pessoas!"]}
