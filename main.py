import 	sys,os,re,
from subprocesses import call, POPEN, STDOUT, PIPE, STDERR
import Tkinter as tk
from DataAnalysis import Operate as op
from USBinterface import Macintosh as mac
from GUI import Application

def main():
	data = mac()
	graphical_analysis = op(data)
	# send to GUI Application and display accordingly
	while data is not None:
		root = tk.Tk()
		app = Application(graphical_analysis,master=root)
		app.mainloop()
		# display output through GUI