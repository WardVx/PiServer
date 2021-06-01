import RPi.GPIO as GPIO
import time

def setup():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(16,GPIO.OUT)
        GPIO.setup(18,GPIO.OUT)
        global PistonU
        global PistonD
        
        PistonU=GPIO.PWM(16,50)
        #Piston omhoog staat hier als poort 11
        #Poort 14 is GROUND
        
        PistonD=GPIO.PWM(18,50)
        #Piston omlaag staat hier als poort 12
        #Poort 20 is GROUND

def PistonUp():
        PistonU.ChangeDutyCycle(10)
        time.sleep(2)
        #Piston gaat gedurende 2 seconden omhoog
        PistonU.ChangeDutyCycle(0)
        
def PistonDown():
        PistonD.ChangeDutyCycle(10)
        time.sleep(2)
        #Piston gaat gedurende 2 seconden omlaag
        PistonD.ChangeDutyCycle(0)
        
def close(): 
         piston.stop()
if __name__ == '__main__':
        setup()
