import RPi.GPIO as GPIO
import time

import lcd_i2c #required to use the LCD, must also have lcd_i2c.py file in the same directory as your script

lcd_i2c.lcd_init() #calls setup function of the LCD


try: #Program will attempt these steps
    #Setup the RaspPi to use the numbering on the board
    GPIO.setmode(GPIO.BCM)

    controlPins = [21, 20, 12, 16]

    # Setup the outputs Pins to control the stepper
    GPIO.setup(controlPins[0], GPIO.OUT)
    GPIO.setup(controlPins[1], GPIO.OUT)
    GPIO.setup(controlPins[2], GPIO.OUT)
    GPIO.setup(controlPins[3], GPIO.OUT)

    # The following matrix should contain the coil energizing sequence for coils A, B, A', and B' 
    halfstepSequence = [ [1,1,0,0],
                         [0,1,0,0],
                         [0,1,1,0],
                         [0,0,1,0],
                         [0,0,1,1],
                         [0,0,0,1],
                         [1,0,0,1],
                         [1,0,0,0],
                         ]

        #We will now go one full rotation - notice you can see the pins turn ON through the LEDs
    for x in range (25): #Range is 25, as it needs 25 cycles through the halfstepSqeuence for a half rotation (each sequence loop represents a rotation of 7.2 degrees)
       
        for halfstep in range (len(halfstepSequence)): #Loop from 0 to len (length) of the half step sequence (8)
            for pin in range (len(controlPins)): #Loop from 0 to len (length) of controlPins (4)
                GPIO.output(controlPins[pin - 1], halfstepSequence[halfstep][pin - 1])
            time.sleep(0.05) #Adjustable for faster or slower speed (too fast and the stepper will stop working), if your connection is slow or you are debugging using the LEDs. Increase the value for slower response.
    time.sleep(5)
        
    for x in range (25): #Range is 25, as it needs 25 cycles through the halfstepSqeuence for a half rotation (each sequence loop represents a rotation of 7.2 degrees)
       
        for halfstep in range (len(halfstepSequence)): #Loop from 0 to len (length) of the half step sequence (8)
            for pin in range (len(controlPins)): #Loop from 0 to len (length) of controlPins (4)
                GPIO.output(controlPins[pin - 1], halfstepSequence[halfstep][pin - 1])
            time.sleep(0.05) #Adjustable for faster or slower speed (too fast and the stepper will stop working), if your connection is slow or you are debugging using the LEDs. Increase the value for slower response.
    time.sleep(5)
    
        #We will now rotate back in the other direction
    for x in range (50): #Range is 50, as it needs 50 cycles through the halfstepSqeuence for a full rotation (each sequence loop represents a rotation of 7.2 degrees)
        for halfstep in reversed (range (len(halfstepSequence))): #Loop from 0 to len (length) of the half step sequence (8)
            for pin in range (len(controlPins)): #Loop from 0 to len (length) of controlPins (4)
                GPIO.output(controlPins[pin - 1], halfstepSequence[halfstep][pin - 1])
            time.sleep(0.05) #Adjustable for faster or slower speed (too fast and the stepper will stop working), if your connection is slow or you are debugging using the LEDs. Increase the value for slower response.


except KeyboardInterrupt: #if interrupted with ctrl+c it breaks out of try statement
    pass

lcd_i2c.printer("Finished. Enjoy", "") #prints to LCD
time.sleep(2)
lcd_i2c.cleanup()#LCD cleanup      
GPIO.cleanup()

