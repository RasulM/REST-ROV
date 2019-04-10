import os   
import time

os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) #needed delay to setup
import pigpio #GPIO library

LeftMotor=4 #pin 7
RightMotor=14 #pin8
UpMotor=24#pin18
Claw= 23#pin16
En= 22#pin15


pi = pigpio.pi();
pi.set_servo_pulsewidth(LeftMotor, 0)
pi.set_servo_pulsewidth(RightMotor, 0)
pi.set_servo_pulsewidth(UpMotor, 0) 

def calibrate(ESCPIN):#This is the auto calibration procedure of a normal ESC
    max_value = 2000 #change this if your ESC's max value is different or leave it be
    min_value = 700  #change this if your ESC's min value is different or leave it be



    pi.set_servo_pulsewidth(ESC, 0)
    print("Disconnect the battery and press Enter")
    inp = input()
    if inp == '':
        pi.set_servo_pulsewidth(ESC, max_value)
        print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
        inp = input()
        if inp == '':            
            pi.set_servo_pulsewidth(ESC, min_value)
            print ("Wierd eh! Special tone")
            time.sleep(7)
            print ("Wait for it ....")
            time.sleep (5)
            print ("Im working on it, DONT WORRY JUST WAIT.....")
            pi.set_servo_pulsewidth(ESC, 0)
            time.sleep(2)
            print ("Arming ESC now...")
            pi.set_servo_pulsewidth(ESC, min_value)
            time.sleep(1)
            print ("See.... uhhhhh")
          # You can change this to any other function you want

def calibrateRovMotor():#This is the auto calibration procedure of a normal ESC
    max_value = 2000 #change this if your ESC's max value is different or leave it be
    min_value = 700  #change this if your ESC's min value is different or leave it be



    pi.set_servo_pulsewidth(LeftMotor, 0)
    pi.set_servo_pulsewidth(RightMotor, 0)
    pi.set_servo_pulsewidth(UpMotor, 0)
    print("Disconnect the battery and press Enter")
    inp = input()
    if inp == '':
        pi.set_servo_pulsewidth(LeftMotor, max_value)
        pi.set_servo_pulsewidth(RightMotor, max_value)
        pi.set_servo_pulsewidth(UpMotor, max_value)
        print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
        inp = input()
        if inp == '':            
            pi.set_servo_pulsewidth(LeftMotor, min_value)
            pi.set_servo_pulsewidth(RightMotor, min_value)
            pi.set_servo_pulsewidth(UpMotor, min_value)
            print ("Wierd eh! Special tone")
            time.sleep(7)
            print ("Wait for it ....")
            time.sleep (5)
            print ("Im working on it, DONT WORRY JUST WAIT.....")
            pi.set_servo_pulsewidth(LeftMotor, 0)
            pi.set_servo_pulsewidth(RightMotor, 0)
            pi.set_servo_pulsewidth(UpMotor, 0)
            time.sleep(2)
            print ("Arming ESC now...")
            pi.set_servo_pulsewidth(LeftMotor, min_value)
            pi.set_servo_pulsewidth(RightMotor, min_value)
            pi.set_servo_pulsewidth(UpMotor, min_value)
            time.sleep(1)
            print("See.... uhhhhh")
          # You can change this to any other function you want
            
def stop(): #This will stop every action your Pi is performing for ESC ofcourse.
    pi.set_servo_pulsewidth(LeftMotor, 0)
    pi.set_servo_pulsewidth(RightMotor, 0) 
    pi.set_servo_pulsewidth(UpMotor, 0)     
    pi.stop()

def up():
    print("Up")
    pi.set_servo_pulsewidth(UpMotor, 1300)
    
def down():
    print("Down")
    pi.set_servo_pulsewidth(UpMotor, 1700)
    
def right():
    print("Right")
    pi.set_servo_pulsewidth(RightMotor, 1300)     
    pi.set_servo_pulsewidth(LeftMotor, 1700)
    
def left():
    print("Left")
    pi.set_servo_pulsewidth(RightMotor, 1700)     
    pi.set_servo_pulsewidth(LeftMotor, 1300)

def backward():
    print("Backward")
    pi.set_servo_pulsewidth(RightMotor, 1700)     
    pi.set_servo_pulsewidth(LeftMotor, 1700)     

def forward():
    print("Forward")
    pi.set_servo_pulsewidth(RightMotor, 1300)     
    pi.set_servo_pulsewidth(LeftMotor, 1300)
    
def still():
    print("Still...")
    pi.set_servo_pulsewidth(RightMotor, 1500)     
    pi.set_servo_pulsewidth(LeftMotor, 1500)
    pi.set_servo_pulsewidth(UpMotor, 1500)

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
    
    
#leftstickFBLR BClawOC RTUp LTDown
forward()
