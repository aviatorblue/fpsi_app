from ImageProcessing import WriteToImage as WTI
from USBinterface import SERIALPORT as SP
from DataAnalysis import Compute as op
import argparse

parser = argparse.ArgumentParser(description='Take data and process it')
parser.add_argument('port', metavar='N', type=str, nargs='1',
                   help='an integer for the accumulator')

args = parser.parse_args()
print args.accumulate(args.integers)

data = SP(args)

graphical_analysis = op.operate(data=data,piezo_conversion=value,)
new_image = WTI(graphical_analysis)
	# send to GUI Application and display accordingly