import tkinter as tk
from src.views.GUI.Page import Page

class SeeRegisteredPeoplePage(Page):
	def __init__(self, data, *args, **kwargs):
		Page.__init__(self, *args, **kwargs)
		self.data = data
