import serial

def SERIALPORT(self,port):
	self.ser = serial.Serial(port, 9600)
	return self.ser





