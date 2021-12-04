import tkinter as tk
from src.views.GUI.Page import Page

class RegisterPersonPage(Page):
	def __init__(self, *args, **kwargs):
		self.onSubmitForm = print
		if ('onSubmitForm' in kwargs.keys()):
			self.onSubmitForm = kwargs['onSubmitForm']
			del kwargs['onSubmitForm']

		Page.__init__(self, *args, **kwargs)
		self.genderOptions = ['', 'Masculino', 'Feminino']
		
		self.__createForm()


	def __createForm(self):
		form = tk.Frame(self)
		form.pack()

		title = tk.Label(
			form,
			text="Página de cadastro",
			font=('Arial', 14, 'bold'),
			pady=30
		)
		title.pack()

		# Name
		nameContainer = tk.Frame(form, pady=10)
		nameContainer.pack(anchor="w")

		nameLabel = tk.Label(
			nameContainer,
			text="Nome: "
		)
		nameLabel.pack(side="left")

		self.nameEntry = tk.Entry(
			nameContainer,
			width=30
		)
		self.nameEntry.pack(side="right")

		# Birth Date
		birthDateContainer = tk.Frame(form, pady=10)
		birthDateContainer.pack(anchor="w")

		birthDateLabel = tk.Label(
			birthDateContainer,
			text="Data de nascimento: "
		)
		birthDateLabel.pack(side="left")

		self.birthDayEntry = tk.Entry(
			birthDateContainer,
			width=2
		)
		self.birthDayEntry.pack(side="left")

		firstSpace = tk.Label(birthDateContainer, text="/")
		firstSpace.pack(side="left")

		self.birthMonthEntry = tk.Entry(
			birthDateContainer,
			width=2
		)
		self.birthMonthEntry.pack(side="left")

		secondSpace = tk.Label(birthDateContainer, text="/")
		secondSpace.pack(side="left")

		self.birthYearEntry = tk.Entry(
			birthDateContainer,
			width=4
		)
		self.birthYearEntry.pack(side="left")

		# Gender
		genderContainer = tk.Frame(form, pady=10)
		genderContainer.pack(anchor="w")

		genderLabel = tk.Label(
			genderContainer,
			text="Sexo: "
		)
		genderLabel.pack(side="left")

		self.genderSelectOptions = tk.StringVar(genderContainer)
		self.genderSelectOptions.set(self.genderOptions[0])

		genderSelect = tk.OptionMenu(
			genderContainer,
			self.genderSelectOptions,
			*self.genderOptions
		)
		genderSelect.pack(side="left")


		# Register
		buttonContainer = tk.Frame(form, pady=20)
		buttonContainer.pack()

		button = tk.Button(
			buttonContainer,
			text="Registrar",
			bg="#4169E1",
			fg="white",
			width=30,
			command=self.__submitForm
		)
		button.pack()


		# Error
		errorContainer = tk.Frame(form)
		errorContainer.pack()

		self.error = tk.Label(errorContainer, font=('Arial', 10))
		self.error.pack()


	def __submitForm(self):
		data = {
			"name": self.nameEntry.get(),
			"birthDate": f'{self.birthYearEntry.get()}-{self.birthMonthEntry.get()}-{self.birthDayEntry.get()}',
			"gender": self.genderSelectOptions.get()
		}

		result = self.onSubmitForm(data)
		if (result['success']):
			self.error['fg'] = "green"
			self.error['text'] = "Cadastro efetuado com sucesso!"
			self.__clearFields()
		else:
			self.error['fg'] = "red"
			self.error['text'] = (" ".join(result['messages']))


	def __clearFields(self):
		self.nameEntry.delete(0, 'end')
		self.birthDayEntry.delete(0, 'end')
		self.birthMonthEntry.delete(0, 'end')
		self.birthYearEntry.delete(0, 'end')
		self.genderSelectOptions.set(self.genderOptions[0])

