import Rpi.GPIO as gpio
import time

gpio.setmode(gpio,BCM)
gpio.setup(21,gpio.out)

while(1):
	gpio.output(21,1)
	print('LED ON')
	time.sleep(2)

	gpio.output(21,0)
	print('LED off')
	time.sleep(2)
gpio.cleanup()
