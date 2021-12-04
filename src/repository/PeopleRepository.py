from src.database import SqliteDatabase

class PeopleRepository:
	def __init__(self):
		self.repository = SqliteDatabase("people.sqlite3")
	

	def getPeople(self):
		sql = """
			SELECT name, birth_date, gender FROM people
			ORDER BY name;
		"""

		try:
			self.repository.cursor.execute(sql)
			result = self.repository.cursor.fetchall()
			
			return result
		except:
			raise Exception('Erro ao obter pessoas do banco de dados!')
	

	def getPersonById(self, id):
		data = (id,)

		sql = "SELECT * FROM people WHERE id = ?;"

		try:
			self.repository.cursor.execute(sql, data)
			result = self.repository.cursor.fetchall()

			return result
		except:
			raise Exception('Erro ao obter pessoa por id do banco de dados!')
	

	def create(self, name, birthDate, gender):
		data = (name, birthDate, gender,)

		sql = """
			INSERT INTO people(name, birth_date, gender)
			VALUES (?,?,?);
		"""

		try:
			self.repository.cursor.execute(sql, data)
			self.repository.db.commit()
		except:
			raise Exception('Erro ao inserir pessoa no banco de dados!')


	def update(self, id, name, birthDate, gender):
		data = (name, birthDate, gender, id,)

		sql = """
			UPDATE people
			SET name = ?, birth_date = ?, gender = ?
			WHERE id = ?;
		"""

		try:
			self.repository.cursor.execute(sql, data)
			self.repository.db.commit()
		except:
			raise Exception('Erro ao atualizar pessoa do banco de dados!')
	

	def delete(self, id):
		data = (id,)

		sql = "DELETE FROM people WHERE id = ?;"

		try:
			self.repository.cursor.execute(sql, data)
			self.repository.db.commit()
		except:
			raise Exception('Erro ao deletar pessoa do banco de dados!')

