import RPi.GPIO as GPIO #Library for the GPIO Pins
import time #Library for time-related tasks

led_list = [16, 12, 1, 7, 8, 25, 24, 23]
GPIO.setmode(GPIO.BCM) #Sets the way we reference the GPIO Pins

for pin in led_list:
    GPIO.setup(pin,GPIO.OUT) #Sets GPIO Pin 'pin' to an output pin


value = 254

#led_list_off = [16,1,8,24,12,7,25,23]

for i in range(value + 1):
    
    for num in led_list:
        check_odd = i % 2
        i//= 2
        if check_odd == 1:
            GPIO.output(num,GPIO.HIGH) #Sets the voltage of Pin 'led' to 'HIGH'
    time.sleep(1)
    for a in led_list:
        GPIO.output(a,GPIO.LOW) #Sets the voltage of Pin 'i' to 'HIGH'

GPIO.cleanup()#Resets the GPIO Pins that we used