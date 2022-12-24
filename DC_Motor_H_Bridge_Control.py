import RPi.GPIO as GPIO #Library for the GPIO Pins
import time #Library for time-related tasks

try: #Program will attempt these steps
    #Setup the RaspPi to use the numbering on the board
    GPIO.setmode(GPIO.BCM) #sets how we reference the GPIO pins

    controlPins = [21, 20] #list of GPIO pin numbers

    # Setup the output pins to control the DC Motor
    GPIO.setup(controlPins[0], GPIO.OUT) #sets pin 21 as an output
    GPIO.setup(controlPins[1], GPIO.OUT) #sets pin 20 as an output
    
    GPIO.output(controlPins[0],GPIO.HIGH) #Sets voltage of Pin 21 to 'HIGH'
    GPIO.output(controlPins[1],GPIO.LOW) #Sets voltage of Pin 20 to 'LOW'
    time.sleep(1) #pauses for 1 second
    
    GPIO.output(controlPins[0],GPIO.LOW) #Sets voltage of Pin 21 to 'LOW'
    GPIO.output(controlPins[1],GPIO.LOW) #Sets voltage of Pin 20 to 'LOW'
    time.sleep(3) #pauses for 3 seconds
    
    GPIO.output(controlPins[1],GPIO.HIGH) #Sets voltage of Pin 20 to 'HIGH'
    GPIO.output(controlPins[0],GPIO.LOW) #Sets voltage of Pin 21 to 'LOW'
    time.sleep(1) #pauses for 1 second
        
except KeyboardInterrupt: #if interrupted with ctrl+c it breaks out of try statement
    pass


       
GPIO.cleanup() #Resets the GPIO Pins that we used
