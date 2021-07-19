
import RPi.GPIO as GPIO
import time
import settings

PistonTravelTime = settings.Piston_Reistijd
PinOn = settings.Pin_Aan
PinUp = settings.Pin_Omhoog
PinDown = settings.Pin_Omlaag

def setup():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(PinOn,GPIO.LOW)
  GPIO.setup(PinUp,GPIO.LOW)
  GPIO.setup(PinDown,GPIO.LOW)

def PistonUp():
  GPIO.setup(PinOn,GPIO.HIGH)
  GPIO.output(PinUp,GPIO.HIGH)
  time.sleep(PistonTravelTime)
  GPIO.setup(PinOn,GPIO.LOW)
  GPIO.output(PinUp,GPIO.LOW)

def PistonDown():
  GPIO.setup(PinOn,GPIO.HIGH)
  GPIO.output(PinDown,GPIO.HIGH)
  time.sleep(PistonTravelTime)
  GPIO.output(PinDown,GPIO.LOW)
  GPIO.setup(PinOn,GPIO.LOW)
        
def close():
        GPIO.cleanup
        print('                   Cleaning up Piston.py')

if __name__ == '__main__':
        try:
                setup()
        except KeyboardInterrupt:
                close()
