import RPi.GPIO as GPIO
import lcd_i2c #required to use the LCD, but lcd_i2c.py must be in same directory as script
import time 
import numpy

print("Setup") #informs user in Python shell that setup is beginning
#General GPIO Pin Setup
GPIO.setmode(GPIO.BCM) #sets how we reference the GPIO pins
GPIO.setup(23, GPIO.OUT) #set the servoPIN to an output

#LCD Setup
lcd_i2c.lcd_init()

#PWM Signal Setup
pin = GPIO.PWM(23,50) #set pin 23 as a PWM output, with a frequency of 50 Hz
pin.start(0) #sets the starting duty cycle of the PWM signal to 0% and initializes the signal
time.sleep(1) #sleep for a second to ensure proper signal initialization

#use of try/except to get out of loop when needed (ctrl + c)
try:
    lcd_i2c.printer("","")
    while True: #starts main loop
        for dutyCycle in numpy.arange (0,101,20): #gives evenly spaced non-integer values within the range
            pin.ChangeDutyCycle(dutyCycle) #changes duty cycle value to updated value in iteration
            lcd_i2c.printer("Duty Cycle: ", str(dutyCycle)) #print message to LCD
            time.sleep(2) #timestep between each change in dutycycle (2 seconds)
            
except KeyboardInterrupt: #stops after (ctrl + c) is pressed 
    # Cleanup after (ctrl + c) is pressed
    print("Cleaning up!") #tells the user cleanup is occuring
    pin.stop() #stops pin 23
    lcd_i2c.cleanup() #cleansup the LCD
    GPIO.cleanup() #cleansup GPIO pins used in the script