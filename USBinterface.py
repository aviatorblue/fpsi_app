import serial

class SERIALPORT():
	def __init__(self,port):
		self.ser = serial.Serial(port, 9600)
		self.port()

	def port(self):
		return self.ser





