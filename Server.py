import Piston2
from socket import *
from datetime import datetime
from time import ctime
import RPi.GPIO as GPIO

timestamp = 1545730073
dt_object = datetime.fromtimestamp(timestamp)
Piston2.setup()

ctrCmd = ['Up','Down']

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
        print(dt_object, " : Wachten")
        tcpCliSock,addr = tcpSerSock.accept()
        print(dt_object, " : Bezig")
        try:
                while True:
                        data = ''
                        data = tcpCliSock.recv(BUFSIZE)
                        if not data:
                                break
                        if data == ctrCmd[0]:
                                print(dt_object, " : Gaat naar boven")
                                Piston2.PistonUp()
                                
                                
                        if data == ctrCmd[1]:
                                print(dt_object, " : Gaat naar beneden")
                                Piston2.PistonDown()
                                
                                
        except KeyboardInterrupt:
                Piston2.close()
                GPIO.cleanup()
tcpSerSock.close();
