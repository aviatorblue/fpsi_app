from ImageProcessing import WriteToImage as WTI
import sys,os,re
from time import strftime as date, sleep
from subprocess import call, Popen
from PIL import Image as IM, ImageTk as ITK
from Tkinter import *
from USBinterface import SERIALPORT as SP
from DataAnalysis import Compute as op
from GUI import Application as App, Error as ERR
from GUIErrors import *
import argparse,sys,os,re

def main():
	try:
		# Set Qualifiers
		root = Tk()
		app = App(master=root)
		mods = app.master

		# Modify GUI features
		mods.title("GUI - Scanning Fabry-Perot Interferometer")
		while True:
			app.update()
			data = SP()
		graphical_analysis = op.operate(data=data,piezo_conversion=value,)
		new_image = WTI(graphical_analysis)
		# send to GUI Application and display accordingly

	except IOError as io:
		print "No Bueno, Me Amigo"

if __name__ == "__main__":
	main()
	sys.exit()