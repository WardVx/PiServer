
import RPi.GPIO as GPIO
import time


def setup():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(23,GPIO.LOW)
  GPIO.setup(24,GPIO.LOW)

def PistonUp():
  GPIO.output(23,GPIO.HIGH)
  time.sleep(2)
  GPIO.output(23,GPIO.LOW)

def PistonDown():
        PistonD.ChangeDutyCycle(10)
        time.sleep(2)
        #Piston gaat gedurende 2 seconden omlaag
        PistonD.ChangeDutyCycle(0)
        
def close():
        GPIO.cleanup
        piston.stop()
        exit

if __name__ == '__main__':
        try:
                setup()
        except KeyboardInterrupt:
                close()
