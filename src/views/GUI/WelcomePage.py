import tkinter as tk
from src.views.GUI.Page import Page

class WelcomePage(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		label = tk.Label(
			self,
			text="Bem vindo ao sistema de cadastro de pessoas com python!",
			font=("Arial", 15, "bold")
		)
		label.pack(side="top", fill="both", expand=True)
