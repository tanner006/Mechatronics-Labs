import RPi.GPIO as GPIO #Library for the GPIO Pins
import time #Library for time-related tasks

GPIO.setmode(GPIO.BCM) #Sets the way we reference the GPIO Pins
GPIO.setup(23,GPIO.OUT) #Sets GPIO Pin 23 to an output pin

for x in range(5): #iterates through the loop 5 times

    print ("LED on") #Prints when the LED turns on in the console below
    GPIO.output(23,GPIO.HIGH) #Sets the voltage of Pin 23 'HIGH' (3.3V)
    time.sleep(5) #Pauses the program for 5 seconds
    print ("LED off") #Prints when the LED turns off in the console below
    GPIO.output(23,GPIO.LOW) #Sets the voltage of Pin 23 'LOW' (0V)
    time.sleep(5) #Pauses the program for 5 seconds
    
GPIO.cleanup()#Resets the GPIO Pins that we used
