import Piston
from socket import *
from time import ctime
import RPi.GPIO as GPIO

Piston.setup()

ctrCmd = ['Up','Down']

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
        print 'Zoeken naar verbinding'
        tcpCliSock,addr = tcpSerSock.accept()
        print 'Verbonden'
        try:
                while True:
                        data = ''
                        data = tcpCliSock.recv(BUFSIZE)
                        if not data:
                                break
                        if data == ctrCmd[0]:
                                Piston.ServoUp()
                                print 'Gaat naar boven'
                        if data == ctrCmd[1]:
                                Piston.ServoDown()
                                print 'Gaat naar beneden'
        except KeyboardInterrupt:
                Piston.close()
                GPIO.cleanup()
tcpSerSock.close();
