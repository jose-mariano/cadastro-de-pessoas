import tkinter as tk
from src.views.GUI.Page import Page

class SeeRegisteredPeoplePage(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		self.tableData = [0, 0, 0, 0, 0, 0, 0]

		self.__createTable()


	def setTableData(self, data):
		self.tableData = data


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
			line = tk.Frame(body)
			line.pack()

			personName = tk.Label(
				line,
				text="José Mariano da Silva",
				width=45,
				font=('Arial', 12),
				anchor="w"
			)
			personName.pack(side="left")

			personBirthDate = tk.Label(
				line,
				text="08/02/2002",
				width=20,
				font=('Arial', 12),
				anchor="w"
			)
			personBirthDate.pack(side="left")

			personGender = tk.Label(
				line,
				text="Masculino",
				width=20,
				font=('Arial', 12),
				anchor="w"
			)
			personGender.pack(side="left")


	def __clearTable(self):
		self.table.destroy()
