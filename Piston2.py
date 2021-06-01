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
  GPIO.output(24,GPIO.HIGH)
  time.sleep(2)
  GPIO.output(24,GPIO.LOW)
  
def close():
  Piston2.stop
if __name__ == '__main__':
  setup()
