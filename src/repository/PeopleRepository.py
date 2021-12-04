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
			raise Exception('Error getting people in database')
	

	def getPersonById(self, id):
		data = (id,)

		sql = "SELECT * FROM people WHERE id = ?;"

		try:
			self.repository.cursor.execute(sql, data)
			result = self.repository.cursor.fetchall()

			return result
		except:
			raise Exception('Error getting person by id in database')
	

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
			raise Exception('Error inserting person in database')


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
			raise Exception('Error updating person in database')
	

	def delete(self, id):
		data = (id,)

		sql = "DELETE FROM people WHERE id = ?;"

		try:
			self.repository.cursor.execute(sql, data)
			self.repository.db.commit()
		except:
			raise Exception('Error deleting person in database')

