import tkinter as tk
from src.views.GUI.Page import Page

class SeeRegisteredPeoplePage(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		self.tableData = list()

		self.__createTable()


	def setTableData(self, data):
		self.tableData = data


	def updateTable(self):
		self.__clearTable()
		self.__createTable()


	def __createTable(self):
		self.table = tk.Frame(self)
		self.table.pack()

		# Header
		header = tk.Frame(self.table)
		header.pack(pady=(20, 0))

		name = tk.Label(
			header,
			text="Nome",
			width=45,
			bg="#4169E1",
			fg="#FFF",
			font=('Arial', 12, 'bold'),
			borderwidth=1,
			relief="ridge"
		)
		name.pack(side="left")

		birthDate = tk.Label(
			header,
			text="Nascimento",
			width=20,
			bg="#4169E1",
			fg="#FFF",
			font=('Arial', 12, 'bold'),
			borderwidth=1,
			relief="ridge"
		)
		birthDate.pack(side="left")

		gender = tk.Label(
			header,
			text="Sexo",
			width=20,
			bg="#4169E1",
			fg="#FFF",
			font=('Arial', 12, 'bold'),
			borderwidth=1,
			relief="ridge"
		)
		gender.pack(side="left")

		# Body
		body = tk.Frame(self.table)
		body.pack()
		
		for person in self.tableData:
			personName = person["name"]
			personBirthDate = person["birthDate"]
			personGender = person["gender"]

			line = tk.Frame(body)
			line.pack()

			labelPersonName = tk.Label(
				line,
				text=personName,
				width=45,
				font=('Arial', 12),
				anchor="w"
			)
			labelPersonName.pack(side="left")

			labelPersonBirthDate = tk.Label(
				line,
				text=personBirthDate,
				width=20,
				font=('Arial', 12),
				anchor="w"
			)
			labelPersonBirthDate.pack(side="left")

			labelPersonGender = tk.Label(
				line,
				text=personGender,
				width=20,
				font=('Arial', 12),
				anchor="w"
			)
			labelPersonGender.pack(side="left")


	def __clearTable(self):
		self.table.destroy()
