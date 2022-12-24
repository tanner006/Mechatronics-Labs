import RPi.GPIO as GPIO #Library for the GPIO Pins
import time #Library for time-related tasks

GPIO.setmode(GPIO.BCM) #Sets the way we reference the GPIO Pins
GPIO.setup(23,GPIO.OUT) #Sets GPIO Pin 23 to an output pin
GPIO.setup(24,GPIO.OUT) #Sets GPIO Pin 24 to an output pin
GPIO.setup(25,GPIO.OUT) #Sets GPIO Pin 25 to an output pin
GPIO.setup(8,GPIO.OUT) #Sets GPIO Pin 8 to an output pin
GPIO.setup(7,GPIO.OUT) #Sets GPIO Pin 7 to an output pin
GPIO.setup(1,GPIO.OUT) #Sets GPIO Pin 1 to an output pin
GPIO.setup(12,GPIO.OUT) #Sets GPIO Pin 12 to an output pin
GPIO.setup(16,GPIO.OUT) #Sets GPIO Pin 16 to an output pin


led_list_on = [23,24,25,8,7,1,12,16]
led_list_off = [16,1,8,24,12,7,25,23]

for led in led_list_on: #

    print ("LED on") #Prints when the LED turns on in the console below
    GPIO.output(led,GPIO.HIGH) #Sets the voltage of Pin 23 'HIGH' (3.3V)
    time.sleep(1) #Pauses the program for 1 second
    


for led in led_list_off:

    
    print ("LED off") #Prints when the LED turns off in the console below
    GPIO.output(led,GPIO.LOW) #Sets the voltage of Pin 23 'LOW' (0V)
    time.sleep(1) #Pauses the program for 1 second

GPIO.cleanup()#Resets the GPIO Pins that we used
