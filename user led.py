import Rpi.GPIO as gpio
import time

gpio.setmode(gpio,BCM)
gpio.setup(21,gpio.OUT)

while(1):
	x=input('Enter the state')
	if x == 'ON':
		gpio.output(21,1)
		print('LED ON')
	if x =='OFF'
		gpio.output(21,0)
		print('LED OFF')
gpio.cleanup()
