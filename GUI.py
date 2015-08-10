import sys,os,re
from time import strftime as date, sleep
from subprocess import call, Popen
from PIL import Image as IM, ImageTk as ITK
from Tkinter import *

class Application(Frame):
	def __init__(self,master=None,port=None,data=None,go=None):
		Frame.__init__(self,master)
		self.port = port
		self.pack()
		self.canvas = Canvas(root, width=1054, height=628, bg="white")
		self.canvas.pack(side="top")
		self.createWidgets()
		self.updateImage()

	def createWidgets(self):

		# Quit Button
		self.QUIT = Button(self, text="QUIT", fg="red",
											command=root.destroy)
		self.QUIT.pack(side="left")

		# Save Image Button
		self.SAVE = Button(self, text="Save Current Image", fg="blue",
						   							command=self.SaveImage)
		self.SAVE.pack(side="left")

		# Input Buffer
		self.e = Entry(master=root)
		self.e.pack(side="left")

		self.e.delete(0, END)
		self.e.insert(0, "Enter Port Location")

		# Get Port Button
		self.GET = Button(self, text="Store Port",fg="black",
						  						command=self.GetPort)
		self.GET.pack(side="left")

		# Pause

	def show_data(self):
		print("Well shoot... there should be data here lol!!!")

	def updateImage(self):
		self.filename = PhotoImage(file="Graph_Update.gif")
		image = self.canvas.create_image(0, 0, anchor=NW, image=self.filename)
		self.canvas.pack(side="top")

	def SaveImage(self):
		saveimage = './images/' + date('%Y-%m-%d_%H%M%S') + '.gif'
		call(['cp','Graph_Update.gif',saveimage])

	def GetPort(self):
		self.port = self.e.get()
		print self.port
		Popen(['python','main.py',self.port])

# Set Qualifiers
root = Tk()
app = Application(master=root)
mods = app.master

# Modify GUI features
mods.title("GUI - Scanning Fabry-Perot Interferometer")
app.mainloop()