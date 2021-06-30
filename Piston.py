
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
  time.sleep(PistonTravelTime)
  GPIO.output(PinUp,GPIO.LOW)

def PistonDown():
  GPIO.output(PinDown,GPIO.HIGH)
  time.sleep(PistonTravelTime)
  GPIO.output(PinDown,GPIO.LOW)
        
def close():
        GPIO.cleanup
        print('Cleaning up Piston.py')

if __name__ == '__main__':
        try:
                setup()
        except KeyboardInterrupt:
                close()
