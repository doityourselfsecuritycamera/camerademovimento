from pyfirmata import Arduino,SERVO
from time import sleep

port = 'COM4'
pinH = 8
pinV = 10
board = Arduino(port)

board.digital[pinH].mode = SERVO
board.digital[pinV].mode = SERVO

def rotateServo(pin,angle):
    board.digital[pin].write(angle)
    sleep(0.070)

    while True:
     for x in range(0,180):
         rotateServo(pinH,x)
     for i in range(180,1,-1):
        rotateServo(pinV, i)


