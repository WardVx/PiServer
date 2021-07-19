import RPi.GPIO as GPIO
import time
import settings

PistonTravelTime = settings.Piston_Reistijd
PinUp = settings.Pin_Omhoog
PinDown = settings.Pin_Omlaag
PinOn = settings.Pin_Aan

def setup():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(PinUp,GPIO.LOW)
  GPIO.setup(PinDown,GPIO.LOW)

def PistonUp():
  GPIO.setup(PinOn,GPIO.HIGH)
  GPIO.output(PinUp,GPIO.HIGH)
  time.sleep(PistonTravelTime)
  GPIO.setup(PinOn,GPIO.LOW)
  GPIO.output(PinUp,GPIO.LOW)

def PistonDown():
  GPIO.output(PinDown,GPIO.HIGH)
  GPIO.setup(PinOn,GPIO.HIGH)
  time.sleep(PistonTravelTime)
  GPIO.setup(PinOn,GPIO.LOW)
  GPIO.output(PinDown,GPIO.LOW)

setup()
try:
    while True:
    PistonUp()
    PistonDown()
    PistonUp()
    PistonDown()
    PistonUp()
    PistonDown()
    print("Test geslaagd")
    GPIO.cleanup()
except KeyboardInterrupt:
    GPIO.cleanup()
