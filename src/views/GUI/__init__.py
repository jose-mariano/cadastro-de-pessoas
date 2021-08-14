import tkinter as tk

class GUI:
	def __init__(self, controller):
		self.controller = controller
		self.config = tk.Tk()
		self.config.wm_geometry("400x400")


	def start(self):
		self.config.mainloop()
