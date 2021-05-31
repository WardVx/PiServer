import RPi.GPIO as GPIO
import time

def setup():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11,GPIO.OUT)
        global PistonU
        global PistonD
        
        PistonU=GPIO.PWM(11,50)
        #Piston omhoog staat hier als poort 11
        
        PistonD=GPIO.PWM(11,50)
        #Piston omlaag staat hier als poort 11

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
