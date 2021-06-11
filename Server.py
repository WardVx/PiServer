import Piston
from socket import *
from datetime import datetime
import datetime
from time import ctime
import time
import RPi.GPIO as GPIO
import sys
import commands

GPIO.setwarnings(False) 
CURSOR_UP_ONE = '\x1b[1A' 
ERASE_LINE = '\x1b[2K' 
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
Piston.setup()
ctrCmd = ['Up','Down']
GetMyIP = commands.getoutput("hostname -I")
HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)
ServerSocket = socket(AF_INET, SOCK_STREAM)
ServerSocket.bind(ADDR)
ServerSocket.listen(5)
ConsoleLOG = 'True'
#Zet de logs in console aan

def CloseServer():
        print '\n'
        print st, ': [SERVER INFO]      Closing...'
        time.sleep(1)
        ServerSocket.close()
        print st, ': [SERVER INFO]      Socket closed'
        Piston.close()
        print st, ': [SERVER INFO]      Piston controller closed'
        GPIO.cleanup()
        print st, ': [SERVER INFO]      GPIO cleaned'
        print st, ': [SERVER INFO]      Cleanup complete'
        print '\n'
        exit

print '\n'
print(' ______ _      _       _                       ______ _ ')
print(' |  ___(_)    | |     | |                      | ___ (_)')
print(' | |_   _  ___| |_ ___| |__  _ __ _   _  __ _  | |_/ /_ ')
print(' |  _| | |/ _ \ __/ __| `_ \| `__| | | |/ _` | |  __/| |')
print(' | |   | |  __/ |_\__ \ |_) | |  | |_| | (_| | | |   | |')
print(' \_|   |_|\___|\__|___/_.__/|_|   \__,_|\__, | \_|   |_|')
print('                                         __/ |          ')
print('   github.com/WardVx                    |___/           ')
print '\n'
print st, ': [SERVER INFO]      Server geladen!'
print st, ': [SERVER INFO]      Server IP :', GetMyIP, PORT
print st, ':                    Wachten...'
def ServerActive():
        while True:
                ClientSocket,addr = ServerSocket.accept()
                if ConsoleLOG == 'True':
                        print st, ': [LOG]              Data ontvangen'
                try:
                        while True:
                                data = ''
                                data = ClientSocket.recv(BUFSIZE)
                                if not data:
                                        print st, ': [LOG]              Geen data ontvangen'
                                        print st, ': [LOG]              Ontvangen data =', data
                                        break
                                if data == ctrCmd[0]:
                                        sys.stdout.write(CURSOR_UP_ONE)
                                        sys.stdout.write(ERASE_LINE) 
                                        print st, ':                    Gaat naar boven'
                                        Piston.PistonUp()
                                        print st, ':                    Wachten...'
                                if data == ctrCmd[1]:
                                        sys.stdout.write(CURSOR_UP_ONE)
                                        sys.stdout.write(ERASE_LINE) 
                                        print st, ':                    Gaat naar beneden'
                                        Piston.PistonDown()
                                        print st, ':                    Wachten...'
                                if ConsoleLOG == 'True':
                                        print st, ': [LOG]              ', data
                except KeyboardInterrupt:
                        CloseServer()


if __name__ == '__main__':
        try:
                ServerActive()
        except KeyboardInterrupt:
                CloseServer()
