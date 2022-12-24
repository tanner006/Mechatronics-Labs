import RPi.GPIO as GPIO #Library for the GPIO Pins
import time #Library for time-related tasks
import lcd_i2c
import numpy #Library for mathematical functions

GPIO.setmode(GPIO.BCM) #sets how we reference the GPIO pins

controlPins = [21, 20, 23] #list of GPIO pin numbers
    
# Setup the outputs Pins to control the DC Motor and LED
GPIO.setup(controlPins[0], GPIO.OUT) #sets pin 21 as an output
GPIO.setup(controlPins[1], GPIO.OUT) #sets pin 20 as an output
GPIO.setup(controlPins[2], GPIO.OUT) #sets pin 23 as an output
pin_21 = GPIO.PWM(controlPins[0],1000) #set pin 21 as a PWM output, with a frequency of 1000 Hz
pin_20 = GPIO.PWM(controlPins[1],1000) #set pin 20 as a PWM output, with a frequency of 1000 Hz

#General LCD Setup
lcd_i2c.lcd_init() #calls setup function of the LCD

#Setup Finished

lcd_i2c.printer("Hello","") #prints to LCD
time.sleep(2) #pauses for 2 seconds
lcd_i2c.printer("","") #prints to LCD
go_clockwise = False
go_counterclockwise = False
try: #Program will attempt these steps
    
    while True: #Continuously running loop
        userinput1 = input("Input a direction (Clockwise or Counterclockwise). Type 'stop' to exit program: \n") #This prompts the user to provide an input and assigns it to the variable userinput1
        if userinput1 == "Clockwise": #evaluates if the user entered a string of "Clockwise"
            go_clockwise = True #alters boolean expression of variable go_clockwise
            lcd_i2c.printer("CW","") #prints to LCD
            go_counterclockwise = False #alters boolean expression of variable go_counterclockwise
        
        elif userinput1 == "Counterclockwise": #evaluates if the user entered a string of "Counterclockwise"
            go_counterclockwise = True #alters boolean expression of variable go_counterclockwise
            lcd_i2c.printer("CCW","") #prints to LCD
            go_clockwise = False #alters boolean expression of variable go_clockwise
        
        elif userinput1 == "stop": #evaluates if the user entered a string of "stop"
            break #This breaks out of the loop if the user entered stop, effectively stopping the program
        
        else:
            print ("Invalid Input, exiting program.") #Prints to the user
            break #exit loop
        
        GPIO.output(23,GPIO.LOW) #Sets voltage of Pin 23 to 'LOW'
        
        if go_clockwise == True:
            pin_21.start(0) #sets the starting duty cycle of the PWM signal to 0% and initializes the signal
            GPIO.output(23,GPIO.HIGH) #Sets voltage of Pin 23 to 'HIGH'
            for dutyCycle in numpy.arange (0,22,1): #gives evenly spaced non-integer values within the range
                pin_21.ChangeDutyCycle(dutyCycle) #changes duty cycle incremently to rotate the DC motor
                time.sleep(0.5) #timestep between each change in dutycycle
            pin_21.stop() #stops pin 21
            lcd_i2c.printer("","") #prints to LCD
            GPIO.output(23,GPIO.LOW) #Sets voltage of Pin 23 to 'LOW'
            go_clockwise == False #alters boolean expression of variable go_clockwise
        
        elif go_counterclockwise == True:
            pin_20.start(0)
            GPIO.output(23,GPIO.HIGH) #Sets voltage of Pin 23 to 'HIGH'
            for dutyCycle_two in numpy.arange (0,22,1): #gives evenly spaced non-integer values within the range
                pin_20.ChangeDutyCycle(dutyCycle_two) #changes duty cycle incremently to rotate the servo
                time.sleep(0.5) #timestep between each change in dutycycle
            pin_20.stop() #stops pin 20
            lcd_i2c.printer("","") #prints to LCD
            GPIO.output(23,GPIO.LOW) #Sets voltage of Pin 23 to 'LOW'
            go_counterclockwise == False #alters boolean expression of variable go_counterclockwise
    

except KeyboardInterrupt: #if interrupted with ctrl+c it breaks out of try statement
    pass

lcd_i2c.printer("Goodbye","") #prints to LCD
time.sleep(2) #pauses for 2 seconds
lcd_i2c.cleanup() #cleansup the LCD
pin_21.stop() #stops pin 21
pin_20.stop() #stops pin 20
GPIO.cleanup() #cleansup GPIO pins used in the script
