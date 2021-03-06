#!/usr/bin/python

import Piston
import settings
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
ctrCmd = ['U','D']
GetMyIP = commands.getoutput("hostname -I")
HOST = ''
PORT = settings.Port
BUFSIZE = 1024
ADDR = (HOST,PORT)
ServerSocket = socket(AF_INET, SOCK_STREAM)
ServerSocket.bind(ADDR)
ServerSocket.listen(1)
ConsoleLOG = settings.Console_LOG

def ServerSetup():
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
        print '                  ',st
        print '[SERVER INFO]      Server geladen!'
        print '[SERVER INFO]      Druk op CTRL + C om te sluiten'
        print '[SERVER INFO]      Server IP :', GetMyIP, PORT
        print '\n'
        print '                   Wachten...'
        Piston.setup()

def ServerActive():
        while True:
                ClientSocket,addr = ServerSocket.accept()
                if ConsoleLOG == 'True':
                        print '[LOG]              Data ontvangen'
                try:
                        while True:
                                data = ''
                                data = ClientSocket.recv(BUFSIZE)
                                if not data:
                                        break
                                if data == ctrCmd[0]:
                                        sys.stdout.write(CURSOR_UP_ONE)
                                        sys.stdout.write(ERASE_LINE) 
                                        print '                   Gaat naar boven'
                                        Piston.PistonUp()
                                        print '                   Wachten...'
                                if data == ctrCmd[1]:
                                        sys.stdout.write(CURSOR_UP_ONE)
                                        sys.stdout.write(ERASE_LINE) 
                                        print '                   Gaat naar beneden'
                                        Piston.PistonDown()
                                        print '                   Wachten...'
                                if ConsoleLOG == 'True':
                                        print '[LOG]             ', data
                except KeyboardInterrupt:
                        CloseServer()

def CloseServer():
        print '\n'
        print '[SERVER INFO]      Closing...'
        ServerSocket.close()
        print '[SERVER INFO]      Socket closed'
        Piston.close()
        print '[SERVER INFO]      Piston controller closed'
        GPIO.cleanup()
        print '[SERVER INFO]      GPIO cleaned'
        print '[SERVER INFO]      Cleanup complete'
        print '\n'
        exit

ServerSetup()

if __name__ == '__main__':
        try:
                ServerActive()
        except KeyboardInterrupt:
                CloseServer()
