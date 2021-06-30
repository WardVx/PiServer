import RPi.GPIO as GPIO
import time
import settings

PistonTravelTime = settings.Piston_Reistijd
PinUp = settings.Pin_Omhoog
PinDown = settings.Pin_Omlaag

def setup():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(PinUp,GPIO.LOW)
  GPIO.setup(PinDown,GPIO.LOW)

def PistonUp():
  GPIO.output(PinUp,GPIO.HIGH)
  time.sleep(1)
  GPIO.output(PinUp,GPIO.LOW)

def PistonDown():
  GPIO.output(PinDown,GPIO.HIGH)
  time.sleep(1)
  GPIO.output(PinDown,GPIO.LOW)

setup()
try:
    while True:
    PistonUp()
    time.sleep(1)
    PistonDown()
    time.sleep(1)
    PistonUp()
    time.sleep(1)
    PistonDown()
    time.sleep(1)
    PistonUp()
    time.sleep(1)
    PistonDown()
    time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
