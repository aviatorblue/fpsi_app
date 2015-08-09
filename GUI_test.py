import sys,os,re
from PIL import Image as IM, ImageTk as ITK
from Tkinter import *

class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()
		self.canvas = Canvas(root, width=850, height=525, bg="black")
		self.canvas.pack()

	def createWidgets(self):
		self.hi_there = Button(self)
		self.hi_there["text"] = "Hello World (click me)"
		self.hi_there["command"] = self.show_data
		self.hi_there.pack(side="top")

		self.QUIT = Button(self, text="QUIT", fg="red",
												command=root.destroy) 
		self.QUIT.pack(side="left")

		self.Update = Button(self)
		self.Update["text"] = "Update Current Image"
		self.Update["command"] = self.updateImage
		self.Update.pack(side="bottom")

	def show_data(self):
		print("Well shoot... there should be data here lol!!!")

	def updateImage(self):
		self.filename = PhotoImage(file='Test.gif')
		image = self.canvas.create_image(50, 50, anchor=NW, image=self.filename)
		self.canvas.pack()


# Set Qualifiers
root = Tk()
app = Application(master=root)
mods = app.master

# Modify GUI features
mods.title("GUI - Scanning Fabry-Perot Interferometer")
app.mainloop()