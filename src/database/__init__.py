import sqlite3 as database

class SqliteDatabase:
	def __init__(self, filename):
		self.db = database.connect(filename)
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

	def save(self):
		self.db.commit()

