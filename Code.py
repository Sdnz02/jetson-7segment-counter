import time
import Jetson.GPIO as GPIO

# 7-SEGMENT
A = 9
B = 11
C = 5
D = 6
DP = 4
E = 13
F = 19
G = 26

switchUpPin = 27
switchDownPin = 22
counter = 0
buttonUpState = 0
lastButtonUpState = 0
buttonDownState = 0
lastButtonDownState = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)
GPIO.setup(E, GPIO.OUT)
GPIO.setup(F, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(DP, GPIO.OUT)
GPIO.setup(switchUpPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switchDownPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(DP, GPIO.LOW)








def changeNumber(buttonPress):
    GPIO.output([A, B, C, D, E, F, G], GPIO.HIGH)
    #time.sleep(0.3) 
    if buttonPress == 0:
        GPIO.output(G, GPIO.LOW)
    elif buttonPress == 1:
        GPIO.output([A, D, E, F, G], GPIO.LOW)
    elif buttonPress == 2:
        GPIO.output([F, C], GPIO.LOW)
    elif buttonPress == 3:
        GPIO.output([ E, F], GPIO.LOW)
    elif buttonPress == 4:
        GPIO.output([A, D, E], GPIO.LOW)
    elif buttonPress == 5:
        GPIO.output([B, E], GPIO.LOW)
    elif buttonPress == 6:
        GPIO.output(B, GPIO.LOW)
    elif buttonPress == 7:
        GPIO.output([ D, E, F, G], GPIO.LOW)
    elif buttonPress == 8:
        GPIO.output([], GPIO.LOW)
    elif buttonPress == 9:
        GPIO.output([ D, E], GPIO.LOW)
    time.sleep(0.1)

try:
    while True:
        buttonUpState = GPIO.input(switchUpPin)
        buttonDownState = GPIO.input(switchDownPin)
	print("switchUpPin: " ,buttonUpState,"/t switchDownPin: ",buttonDownState)
        print(counter)
        if buttonUpState != lastButtonUpState:
            if buttonUpState == GPIO.HIGH:
		counter += 1                
		if counter >= 9:
                    counter = 9

                #print(counter)
                time.sleep(0.3)
            else:
                print("ON")
            time.sleep(0.05)

        if buttonDownState != lastButtonDownState:
            if buttonDownState == GPIO.HIGH:
                counter -= 1                
		if counter <= 0:
                    counter = 0
                #print(counter)
                time.sleep(0.3)
            else:
                print("ON")
            time.sleep(0.05)

        changeNumber(counter)

finally:
    GPIO.cleanup()