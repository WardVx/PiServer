import Piston2
from socket import *
from datetime import datetime
import datetime
from time import ctime
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False) 

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

print(st, "Server Loaded!")
print(" ")

while True:
        print(st, " : Wachten")
        tcpCliSock,addr = tcpSerSock.accept()
        print(st, " : Bezig")
        try:
                while True:
                        data = ''
                        data = tcpCliSock.recv(BUFSIZE)
                        if not data:
                                print(st, " : Niets ontvangen")
                                break
                        if data == ctrCmd[0]:
                                print(st, " : Gaat naar boven")
                                Piston2.PistonUp()
                                
                                
                        if data == ctrCmd[1]:
                                print(st, " : Gaat naar beneden")
                                Piston2.PistonDown()
                                
                                
        except KeyboardInterrupt:
                Piston2.close()
                GPIO.cleanup()
tcpSerSock.close();
