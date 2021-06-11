
import RPi.GPIO as GPIO
import time

PistonTravelTime = 2


def setup():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(23,GPIO.LOW)
  GPIO.setup(24,GPIO.LOW)

def PistonUp():
  GPIO.output(23,GPIO.HIGH)
  time.sleep(PistonTravelTime)
  GPIO.output(23,GPIO.LOW)

def PistonDown():
  GPIO.output(23,GPIO.HIGH)
  time.sleep(PistonTravelTime)
  GPIO.output(23,GPIO.LOW)
        
def close():
        GPIO.cleanup
        piston.stop()

if __name__ == '__main__':
        try:
                setup()
        except KeyboardInterrupt:
                close()
