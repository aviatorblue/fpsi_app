import sys,os,re
from PIL import Image, ImageTk
import Tkinter as tk

class Application(tk.Frame):
	def __init__(self,master=None):
		tk.Frame.__init__(self,master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.hi_there = tk.Button(self)
		self.hi_there["text"] = "Hello World (click me)"
		self.hi_there["command"] = self.show_data
		self.hi_there.pack(side="top")

		self.QUIT = tk.Button(self, text="QUIT", fg="red",
												command=root.destroy) 
		self.QUIT.pack(side="left")

	def show_data(self):
		print("Well shoot... there should be data here lol!!!")

# Set Qualifiers
root = tk.Tk()
app = Application(master=root)
mods = app.master

# Modify GUI features
mods.title("GUI - Scanning Fabry-Perot Interferometer")
img = ImageTk.PhotoImage(Image.open("Test.gif"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
app.mainloop()