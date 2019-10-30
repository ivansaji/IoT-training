import Rpi.GPIO as gpio
# RPI gpio library
import time
#module for time
import random
# module for randomised number

gpio.setmode(gpio,BCM)	#used to set the RPI mode
gpio.setup(21,gpio.OUT) #used to set pin as output

while(1):
    a = input("ON or OFF\n")
    if a == 'ON':
        gpio.output(21,1)	
	    print('buzzer ON')
	    time.sleep(2)
        gpio.output(21,0)
    elif a == 'OFF':
        gpio.output(21,0)	
    else:
        print("Invalid value")
        gpio.output(21,0)
	
gpio.cleanup()			# clear existing states of GPIO
