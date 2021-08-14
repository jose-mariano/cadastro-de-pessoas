import tkinter as tk
from src.views.GUI.WelcomePage import WelcomePage
from src.views.GUI.RegisterPersonPage import RegisterPersonPage
from src.views.GUI.SeeRegisteredPeoplePage import SeeRegisteredPeoplePage

class GUI:
	def __init__(self, controller):
		self.controller = controller
		self.config = tk.Tk()
		self.config.title("Cadastro de pessoas")
		self.config.wm_geometry("800x400")
		self.config.resizable(height=False, width=False)
		self.config.tk_setPalette(
			background="#FFF",
			foreground="#000",
			activeBackground="#191970",
			activeForeground="#FFF"
		)


	def __createPages(self):
		buttonframe = tk.Frame(self.config, bg='white')
		buttonframe.pack(side="top", fill="x", expand=False)

		container = tk.Frame(self.config)
		container.pack(side="top", fill="both", expand=True)

		# Config pages
		welcomePage = WelcomePage(self.config)
		welcomePage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

		registerPersonPage = RegisterPersonPage(self.config)
		registerPersonPage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

		seeRegisteredPeoplePage = SeeRegisteredPeoplePage(self.config)
		seeRegisteredPeoplePage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)


		# Config buttons
		registerPersonPageButton = tk.Button(
			buttonframe,
			text="Cadastrar",
			bg="#4169E1",
			fg="white",
			width=20,
			command=registerPersonPage.show
		)
		registerPersonPageButton.pack(side="left", expand=True)

		seeRegisteredPeoplePageButton = tk.Button(
			buttonframe,
			text="Ver pessoas cadastradas",
			bg="#4169E1",
			fg="white",
			width=20,
			command=seeRegisteredPeoplePage.show
		)
		seeRegisteredPeoplePageButton.pack(side="right", expand=True)


		# Start default page
		welcomePage.show()


	def start(self):
		self.__createPages()
		self.config.mainloop()
