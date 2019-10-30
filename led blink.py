import Rpi.GPIO as gpio
# RPI gpio library
import time
#module for time

gpio.setmode(gpio,BCM)	#used to set the RPI mode
gpio.setup(21,gpio.OUT) #used to set pin as output

while(1):
	gpio.output(21,1)	#turn on LED(pin number, state)
	print('LED ON')
	time.sleep(2) 		#turn OFF LED	

	gpio.output(21,0)
	print('LED off')
	time.sleep(2)
gpio.cleanup()			# clear existing states of GPIO
