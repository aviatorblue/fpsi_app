import sys,os,re
from time import strftime as date, sleep
from subprocess import call, Popen
from PIL import Image as IM, ImageTk as ITK
from Tkinter import *

class Application(Frame):
	def __init__(self,master=None,port=None,data=None,go=None):
		Frame.__init__(self,master,width=1000,height=400,bd=1)
		self.port = port
		self.pack()
		self.createWidgets()
		self.updateImage()
		self.display_port()

	def createWidgets(self):
		iframe1 = Frame(self,bd=2,relief=SUNKEN)
		# Quit Button
		self.QUIT = Button(iframe1, text="QUIT", fg="red",
											command=root.destroy)
		self.QUIT.pack(side=LEFT, padx=5)

		# Save Image Button
		self.SAVE = Button(iframe1, text="Save Current Image", fg="blue",
						   							command=self.SaveImage)
		self.SAVE.pack(side=LEFT, padx=5)

		# Input Buffer

		# Get Port Button
		self.GET = Button(iframe1, text="Store Port",fg="black",
						  						command=self.GetPort)
		self.GET.pack(side=RIGHT, padx=5)

		self.e = Entry(iframe1)
		self.e.pack(side=RIGHT, padx=0)

		self.e.delete(0, END)
		self.e.insert(0, "Enter Port Location")

		iframe1.pack(expand=1, fill=X, pady=10, padx=5)

	def show_data(self):
		print("Well shoot... there should be data here lol!!!")

	def updateImage(self):
		iframe2 = Frame(self,bd=2,relief=SUNKEN)
		self.canvas = Canvas(iframe2, width=1054, height=628, bg="white")
		self.filename = PhotoImage(file="Graph_Update.gif")
		image = self.canvas.create_image(0, 0, anchor=NW, image=self.filename)
		self.canvas.pack(side="top")
		iframe2.pack(expand=1, fill=X, pady=10, padx=5)

	def SaveImage(self):
		saveimage = './images/' + date('%Y-%m-%d_%H%M%S') + '.gif'
		call(['cp','Graph_Update.gif',saveimage])

	def GetPort(self):
		self.port = self.e.get()
		info = open("./docs/info.txt",'w')
		string = "Port: " + self.port
		info.write(string)
		info.close()
		self.name_label.config(text=string)

	def display_port(self):
		try:
			self.sframe = Frame(self,bd =2)
			info = open("./docs/info.txt",'r')
			self.port_name = info.read()
			self.name_label = Label(self.sframe, text=self.port_name)
			self.name_label.pack()
			self.sframe.pack(expand=1, fill=X)
		except IndexError as ie:
			port = "None selected"
			self.name_label = Label(self.sframe, text=self.port_name)
			self.name_label.pack()
			self.sframe.pack(expand=1, fill=X)

class Error(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.canvas = Canvas(root, width=500, height=100, bg="white")
		self.canvas.pack(side="top")
		self.createWidgets()

	def createWidgets(self):

		# Quit Button
		self.QUIT = Button(self, text="Well that sucks", fg="red",
											command=root.destroy)
		self.QUIT.pack(side="right")

		# Pause

root = Tk()
app = Application(master=root)
mods = app.master

mods.title("GUI - Scanning Fabry-Perot Interferometer")

app.mainloop()