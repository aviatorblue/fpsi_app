from ImageProcessing import WriteToImage as WTI
from USBinterface import SERIALPORT as SP
from DataAnalysis import Compute as op
from GUIErrors import *
import argparse,sys,os,re

def main():
	try:
		parser = argparse.ArgumentParser(description='Take data and process it')
		parser.add_argument('port', metavar='N', type=str, nargs='1',
    	               help='an integer for the accumulator')
		args = parser.parse_args()

		data = SP(args)
		graphical_analysis = op.operate(data=data,piezo_conversion=value,)
		new_image = WTI(graphical_analysis)
		# send to GUI Application and display accordingly

	except IOError as io:
		print "No Bueno, Me Amigo"

	except DataError as de:



if __name__ == "__main__":
	main()
	sys.exit()