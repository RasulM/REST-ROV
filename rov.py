import os   
import time

os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) #needed delay to setup
import pigpio #GPIO library
#White motor controller
LIn1=4#pin 7
LIn2=3#pin 5
LEnA=2#pin 3
RIn3=14#pin8
RIn4=15#pin 10
REnB=18#pin 12
#black motor controller
UpM=24#pin18 m1
UpEn=10#pin19 e1
Claw=23#pin16 -> m2
En= 22#pin15 -> e2


pi = pigpio.pi();

            
def stop(): #This will stop every action your Pi is performing for ESC ofcourse.
    pi.stop()

def up():
    print("Up")
    pi.write(UpMotor, 1)
    pi.write(UpEn,1)
    time.sleep(2)
    pi.write(UpEn,0)
    
def down():
    print("Down")
    pi.write(UpM, 0)
    pi.write(UpEn,1)
    time.sleep(2)
    pi.write(UpEn,0)
    
def right():
    print("Right")
    pi.write(RIn1,0)
    pi.write(RIn2,1)
    pi.write(REnB,1)
    time.sleep(2)
    pi.write(REnB,0)

def left():
    print("Left")
    pi.write(LIn1,0)
    pi.write(LIn2,1)
    pi.write(LEnB,1)
    time.sleep(2)
    pi.write(LEnB,0)

def backward():
    print("Backward")
    pi.write(RIn1,0)
    pi.write(RIn2,1)
    pi.write(LIn1,0)
    pi.write(LIn2,1)
    pi.write(LEnB,1)
    pi.write(REnB,1)
    time.sleep(2)
    pi.write(REnB,0)   
    pi.write(LEnB,0)

def forward():
    print("Forward")
    pi.write(RIn1,1)
    pi.write(RIn2,0)
    pi.write(LIn1,1)
    pi.write(LIn2,0)
    pi.write(LEnB,1)
    pi.write(REnB,1)
    time.sleep(2)
    pi.write(REnB,0)   
    pi.write(LEnB,0)
    
def still():
    print("Still...")
    pi.write(REnB,0)   
    pi.write(LEnB,0)

def openclaw():
    print("Open")
    pi.write(Claw, 0)
    pi.write(En,1)
    time.sleep(2)
    pi.write(En,0)
def closeclaw():
    print("Close")
    pi.write(Claw, 1)
    pi.write(En,1)
    time.sleep(2)
    pi.write(En,0)
