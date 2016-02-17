import serial
import time

arduino = serial.Serial(port="/dev/ttyMFD1", baudrate=9600)

while True:
	sendstr = "What's up"
	print "To Arduino:", sendstr
	arduino.write(sendstr)
	time.sleep(1)

	print "From Arduino:", arduino.read(arduino.in_waiting)

	time.sleep(1)
	print

