import 	sys,os,re,
from subprocesses import call, POPEN, STDOUT, PIPE, STDERR
import Tkinter as tk


def main():
	graphical_analysis = op(data)
	new_image = WriteToImage(graphical_analysis)
	# send to GUI Application and display accordingly
	root = tk.Tk()
	app = Application(path="Data_Graph.gif",master=root)
	mods = app.master

	# Modify GUI features
	mods.title("GUI - Scanning Fabry-Perot Interferometer")
	app.mainloop()