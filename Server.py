import Piston2
from socket import *
from time import ctime
import RPi.GPIO as GPIO

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
        print 'Wachten'
        tcpCliSock,addr = tcpSerSock.accept()
        print 'Bezig'
        try:
                while True:
                        data = ''
                        data = tcpCliSock.recv(BUFSIZE)
                        if not data:
                                break
                        if data == ctrCmd[0]:
                                Piston2.ServoUp()
                                print 'Gaat naar boven'
                                time.sleep(2)
                        if data == ctrCmd[1]:
                                Piston2.ServoDown()
                                print 'Gaat naar beneden'
                                time.sleep(2)
        except KeyboardInterrupt:
                Piston2.close()
                GPIO.cleanup()
tcpSerSock.close();
