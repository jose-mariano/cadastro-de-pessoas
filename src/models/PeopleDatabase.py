import sqlite3 as database

class PeopleDatabase:
	def __init__(self, dbPath):
		self.db = database.connect(dbPath)

