import time
import RPi.GPIO as GPIO
import lcd_i2c #required to use the LCD, must also have lcd_i2c.py file in the same directory as your script
print("Setup") #informs user setup has begun

#General GPIO Setup
GPIO.setmode(GPIO.BCM) #sets how we reference GPIO pins
GPIO.setup(23, GPIO.OUT) #sets GPIO pin 23 as an output

#PWM Signal Setup
pin = GPIO.PWM(23,500) #set pin 23 as a PWM output, with a frequency of 500 Hz
pin.start(0) #sets the starting duty cycle of the PWM signal to 0% and initializes the signal
time.sleep(1) #sleep for a second to ensure signal is initialized properly

#General LCD Setup
lcd_i2c.lcd_init() #calls setup function of the LCD

print("Begin") #informs user the main function of the program is beginning

#Main portion of program

#Determining string inputs for LCD, the first string is static, in the second string we use variables as inputs
inputstring1 = "Welcome" #The string we send to the first line of the LCD
inputstring2 = "" #Empty String
inputstring3 = "Goodbye"

pin.ChangeDutyCycle(50) #changes the duty cycle to 50%

try:    
    lcd_i2c.printer(inputstring1,"") #prints to LCD
    time.sleep(2)#sleep for 2 seconds
    lcd_i2c.printer(inputstring2,"") #prints to LCD
    time.sleep(8)#sleep for 8 seconds
    lcd_i2c.printer(inputstring3,"") #prints to LCD
    time.sleep(2)#sleep for 2 seconds
except KeyboardInterrupt: #stops try if (ctrl + c) is pressed
    pass
pin.stop() #stops the pin initialization

GPIO.cleanup() #cleansup all of the GPIO pins used within the script
lcd_i2c.cleanup()#LCD cleanup
print("Done") #informs the user the program is finished running

