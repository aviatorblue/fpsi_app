#from ImageProcessing import WriteToImage as WTI
import sys,os,re
from time import strftime as date, sleep
from subprocess import call, Popen
from PIL import Image as IM, ImageTk as ITK
from Tkinter import *
from USBinterface import SERIALPORT as SP
#from DataAnalysis import Compute as op
#from GUIErrors import *
import argparse,sys,os,re

class Application(Frame):
	def __init__(self,master=None,port=None,data=None,go=None):
		Frame.__init__(self,master,width=1000,height=400,bd=1)
		self.image = "Graph_Update.gif"
		#self.error = Error(master=root)
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

	def updateImage(self):
		iframe2 = Frame(self,bd=2,relief=SUNKEN)

		self.canvas = Canvas(iframe2, width=1054, height=628, bg="white")
		self.filename = PhotoImage(file=self.image)
		image = self.canvas.create_image(0, 0, anchor=NW, image=self.filename)
		self.canvas.pack(side="top")

		# Pause
		self.pause = Button(iframe2, text="PAUSE", fg="black",bg="red",command=self.PauseImage)
		self.pause.pack(side=RIGHT,padx=5)

		# Start
		self.current = Button(iframe2, text="START",fg="black",bg="green",command=self.CurrentImage)
		self.current.pack(side=RIGHT,padx=5)

		iframe2.pack(expand=1, fill=X, pady=10, padx=5)

	def SaveImage(self):
		save_image = './images/' + date('%Y-%m-%d_%H%M%S') + '.gif'
		call(['cp','Graph_Update.gif',save_image])

	def PauseImage(self):
		self.pause_image = './images/pause/' + date('%Y-%m-%d_%H%M%S') + '.gif'
		call(['cp','Graph_Update.gif',self.pause_image])
		self.image = self.pause_image

	def CurrentImage(self):
		self.image = "Graph_Update.gif"

	def GetPort(self):
		self.port = self.e.get()
		info = open("./docs/info.bin",'w')
		string = "Port: " + self.port
		info.write(string)
		info.close()
		self.name_label.config(text=string)

	def display_port(self):
		try:
			self.sframe = Frame(self,bd =2)
			info = open("./docs/info.bin",'r')
			self.port_name = info.read()
			self.name_label = Label(self.sframe, text=self.port_name)
			self.name_label.pack()
			self.sframe.pack(expand=1, fill=X)
		except IndexError as ie:
			port = "Port: None Selected"
			self.name_label = Label(self.sframe, text=port)
			self.name_label.pack()
			self.sframe.pack(expand=1, fill=X)
		except IOError as INOUT:
			port = "Port: None Selected"
			self.name_label = Label(self.sframe, text=port)
			self.name_label.pack()
			self.sframe.pack(expand=1, fill=X)

class Error(Frame):
	def __init__(self,master=None,variable=None):
		Frame.__init__(self,master)
		self.variable = variable
		self.pack()
		self.canvas = Canvas(root, width=500, height=100, bg="white")
		self.canvas.pack(side="top")
		self.createWidgets()

	def createWidgets(self):

		text = self.variable
		err = "ERROR: " + text
		# Quit Button
		self.QUIT = Button(self, text=err, fg="red",
											command=root.destroy)
		self.QUIT.pack(side="right")

def main():
	try:
		# Set Qualifiers
		app = Application(master=root)
		mods = app.master

		# Modify GUI features
		mods.title("GUI - Scanning Fabry-Perot Interferometer")
		app.mainloop()
		# send to GUI Application and display accordingly

	except IOError as io:
		print "No Bueno, Me Amigo"

if __name__ == "__main__":
	root = Tk()
	main()
	sys.exit()