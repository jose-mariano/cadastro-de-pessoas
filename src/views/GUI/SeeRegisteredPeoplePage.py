import tkinter as tk
from src.views.GUI.Page import Page

class SeeRegisteredPeoplePage(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		self.size = 10
		self.tableData = [[]]
		self.currentPage = 1

		self.__createTable()


	def setTableData(self, data):
		newData = [[]]
		lenNewData = len(newData)
		for item in data:
			newData[lenNewData - 1].append(item)

			if (len(newData[lenNewData - 1]) == self.size):
				newData.append([])
				lenNewData += 1

		self.tableData = newData


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
		
		for person in self.tableData[self.currentPage - 1]:
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

		# Footer
		footer = tk.Frame(self.table)
		footer.pack(pady=5)

		buttonFirstPage = tk.Button(
			footer,
			bg="#4169E1",
			fg="#FFF",
			font=('Arial', 10, 'bold'),
			text="<<",
			command=self.__firstPage
		)
		buttonFirstPage.pack(side="left")

		buttonBackPage = tk.Button(
			footer,
			bg="#4169E1",
			fg="#FFF",
			font=('Arial', 10, 'bold'),
			text="<",
			command=self.__backPage
		)
		buttonBackPage.pack(side="left")

		currentPage = tk.Label(
			footer,
			width=4,
			height=2,
			font=('Arial', 12, 'bold'),
			text=self.currentPage
		)
		currentPage.pack(side="left")

		buttonLastPage = tk.Button(
			footer,
			bg="#4169E1",
			fg="#FFF",
			font=('Arial', 10, 'bold'),
			text=">>",
			command=self.__lastPage
		)
		buttonLastPage.pack(side="right")

		buttonNextPage = tk.Button(
			footer,
			bg="#4169E1",
			fg="#FFF",
			font=('Arial', 10, 'bold'),
			text=">",
			command=self.__nextPage
		)
		buttonNextPage.pack(side="right")


	def __nextPage(self):
		if ((self.currentPage + 1) <= len(self.tableData)):
			self.currentPage += 1
			self.updateTable()


	def __backPage(self):
		if ((self.currentPage - 1) >= 1):
			self.currentPage -= 1
			self.updateTable()


	def __lastPage(self):
		lengthTableData = len(self.tableData)
		if (self.currentPage != lengthTableData):
			self.currentPage = lengthTableData
			self.updateTable()


	def __firstPage(self):
		if (self.currentPage != 1):
			self.currentPage = 1
			self.updateTable()


	def __clearTable(self):
		self.table.destroy()
