import Rpi.GPIO as gpio
import time

gpio.setmode(gpio,BCM)

trig = 21       #initialized trigger & echo pins
echo = 20
gpio.setup(trig,gpio.OUT)   #set trig pin as output
gpio.setup(echo,gpio.IN)    # set echo pin as Input

gpio.output(trig,False)     # clearing off the trigger pin
print("Waiting for sensor to settle")
time.sleep(2)

while(True):
    gpio.output(trig,True)      # line 16 to 18 creates a pulse
    time.sleep(0.0001)
    gpio.output(trig,False)
    while gpio.input(echo)==0:  #used to mark start time
        pulse_start = time.time()
    while gpio.input(echo)==1:      # used to mark end time
        pulse_end = time.time()

    