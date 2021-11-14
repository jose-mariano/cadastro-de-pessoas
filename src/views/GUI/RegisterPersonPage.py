import tkinter as tk
from src.views.GUI.Page import Page

class RegisterPersonPage(Page):
	def __init__(self, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		label = tk.Label(self, text="Página para cadastrar uma pessoa!")
		label.pack(side="top", fill="both", expand=True)
