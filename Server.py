import Piston2
from socket import *
from datetime import datetime
import datetime
from time import ctime
import time
import RPi.GPIO as GPIO
import sys

GPIO.setwarnings(False) 

CURSOR_UP_ONE = '\x1b[1A' 
ERASE_LINE = '\x1b[2K' 

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
Piston2.setup()

ctrCmd = ['Up','Down']

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
print '\n'
print(' ______ _      _       _                       ______ _ ')
print(' |  ___(_)    | |     | |                      | ___ (_)')
print(' | |_   _  ___| |_ ___| |__  _ __ _   _  __ _  | |_/ /_ ')
print(' |  _| | |/ _ \ __/ __| `_ \| `__| | | |/ _` | |  __/| |')
print(' | |   | |  __/ |_\__ \ |_) | |  | |_| | (_| | | |   | |')
print(' \_|   |_|\___|\__|___/_.__/|_|   \__,_|\__, | \_|   |_|')
print('                                         __/ |          ')
print('                                        |___/           ')
print '\n'
print st, ' : Server geladen!'

while True:
        print st, ' : Wachten...', '\r'
        tcpCliSock,addr = tcpSerSock.accept()

        try:
                while True:
                        data = ''
                        data = tcpCliSock.recv(BUFSIZE)
                        if not data:
                                print ctrCmd
                                print st, ' : Error! Geen data ontvangen!'
                                break
                        if data == ctrCmd[0]:
                                sys.stdout.write(CURSOR_UP_ONE)
                                sys.stdout.write(ERASE_LINE) 
                                print st, ' : Gaat naar boven'
                                Piston2.PistonUp()
                                
                                
                        if data == ctrCmd[1]:
                                sys.stdout.write(CURSOR_UP_ONE)
                                sys.stdout.write(ERASE_LINE) 
                                print st, ' : Gaat naar beneden'
                                Piston2.PistonDown()
                                
                                
        except KeyboardInterrupt:
                Piston2.close()
                GPIO.cleanup()
tcpSerSock.close();
