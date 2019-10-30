import Rpi.GPIO as gpio
# RPI gpio library
import time
#module for time
import random
# module for randomised number

gpio.setmode(gpio,BCM)	#used to set the RPI mode
gpio.setup(21,gpio.OUT) #used to set pin as output

while(1):
    otp = random.randint(10000,99999)
    print('OTP is' + otp)

    a = int(input("Enter the OTP"))
    if a == otp:
        print("OTP Accepted")
        gpio.output(21,1)	
	    print('LED ON')
	    time.sleep(2)
        gpio.output(21,0)	
    else:
        print("Invalid OTP")
        gpio.output(21,0)
	
gpio.cleanup()			# clear existing states of GPIO
