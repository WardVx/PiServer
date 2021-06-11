
import RPi.GPIO as GPIO
import time

PistonTravelTime = 2
#Minimum tijd dat de piston moet bewegen
PinUp = 23
#Nummer van de pin die OMHOOG doorgeeft
PinDown = 24
#Nummer van de pin die OMLAAG aangeeft

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
        piston.stop()

if __name__ == '__main__':
        try:
                setup()
        except KeyboardInterrupt:
                close()
