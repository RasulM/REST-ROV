#import evdev
from evdev import InputDevice, categorize, ecodes
import rov

#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event0')

#button code variables (change to suit your device)
aBtn = 34
bBtn = 305
xBtn = 35
yBtn = 23

up = 46
down = 32
left = 18
right = 33

start = 24
select = 49

lTrig = 310
rTrig = 311

LX = 0
LY = 1
#prints out device info at start
print(gamepad)
rov.calibrateRovMotor()
#loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    if event.type == ecodes.EV_ABS:
        if event.value == 0:
            if event.code == LX:
                rov.left()
            elif event.code == LY:
                rov.up()
        elif event.value == 255:
            if event.code == LX:
                rov.right()
            elif event.code == LY:
                rov.down()
            
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
          #  if event.code == yBtn:
            #    print("Y")
                
            if event.code == bBtn:
                print("B")
                rov.closeclaw()
                
            elif event.code == aBtn:
               print("A")
               rov.openclaw()
          #  elif event.code == xBtn:
           #     print("X")

           # elif event.code == up:
           #     print("up")
           # elif event.code == down:
             #   print("down")
           # elif event.code == left:
           #     print("left")
           # elif event.code == right:
             #   print("right")

          #  elif event.code == start:
          #      print("start")
          #  elif event.code == select:
            #    print("select")

            elif event.code == lTrig:
                print("Down")
                rov.down
            elif event.code == rTrig:
                print("Up")
                rov.up
