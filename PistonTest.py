import RPi.GPIO as GPIO
import time
import settings

PistonTravelTime = settings.Piston_Reistijd
PinUp = settings.Pin_Omhoog
PinDown = settings.Pin_Omlaag

def setup():
  GPIO.cleanup
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(PinUp,GPIO.LOW)
  GPIO.setup(PinDown,GPIO.LOW)
  

def PistonUp():
  GPIO.output(PinOn,GPIO.HIGH)
  GPIO.output(PinUp,GPIO.HIGH)
  time.sleep(PistonTravelTime)
  GPIO.output(PinOn,GPIO.LOW)
  GPIO.output(PinUp,GPIO.LOW)

def PistonDown():
  GPIO.output(PinDown,GPIO.HIGH)
  time.sleep(PistonTravelTime)
  GPIO.output(PinDown,GPIO.LOW)

try:
    while True:
      setup()
      PistonUp()
      PistonDown()
      PistonUp()
      PistonDown()
      PistonUp()
      PistonDown()
      print("Test geslaagd")
      close()
except KeyboardInterrupt:
    close()
def close():
  GPIO.cleanup()