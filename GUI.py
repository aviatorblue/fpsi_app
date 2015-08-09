import sys,os,re
import Tkinter as tk

class Application(tk.Frame):
	def __init__(self,data,master=None):
		tk.Frame.__init__(self,master)
		self.pack()
		self.createWidgets(data)

	def createWidgets(self,data):
		self.hi_there = tk.Button(self)
		self.hi_there["text"] = "Hello World (click me)"
		self.hi_there["command"] = self.show_data(data)
		self.hi_there.pack(side="top")

		self.QUIT = tk.Button(self, text="QUIT", fg="red",
												command=root.destroy) 
		self.QUIT.pack(side="bottom")

	def show_data(self,data):
		print data
		print("Well shoot... there should be data here lol!!!")

# Set Qualifiers
root = tk.Tk()
app = Application([1,2,3,4,5,6],master=root)
app.mainloop()