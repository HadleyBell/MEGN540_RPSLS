from gpiozero import OutputDevice, Servo, Button
import gpiozero
from time import sleep

# Pins 
# Servo
myGPIO_l = 16 #left
myGPIO_r = 12 #right
# Stepper
coil_A_1 = OutputDevice(23)
coil_A_2 = OutputDevice(24)
coil_B_1 = OutputDevice(27)
coil_B_2 = OutputDevice(22)
# Limit Switch
limit = Button(4)
# Buttons
button1 = Button(5) # start
button2 = Button(6) # stop
button3 = Button(13) # reset


time_delay = 0.005

servo_l = Servo(myGPIO_l)
servo_r = Servo(myGPIO_r)
 
def servo_cmd():
    while True:

        servo_l.mid()
        print("mid")
        sleep(1)
        servo_l.min()
        print("min")
        sleep(1)
        servo_l.mid()
        print("mid")
        sleep(1)
        servo_l.max()
        print("max")
        sleep(1)


def step_forward():

    coil_A_1.on()
    coil_A_2.off()
    coil_B_1.on()
    coil_B_2.off()
    sleep(time_delay)

    coil_A_1.on()
    coil_A_2.off()
    coil_B_1.off()
    coil_B_2.on()
    sleep(time_delay)

    coil_A_1.off()
    coil_A_2.on()
    coil_B_1.off()
    coil_B_2.on()
    sleep(time_delay)

    coil_A_1.off()
    coil_A_2.on()
    coil_B_1.on()
    coil_B_2.off()
    sleep(time_delay)

    coil_A_1.off()
    coil_A_2.off()
    coil_B_1.off()
    coil_B_2.off()


def step_backwards():

    # step 3
    coil_A_1.off()
    coil_A_2.on()
    coil_B_1.off()
    coil_B_2.on()
    sleep(time_delay)

    # step 4
    coil_A_1.on()
    coil_A_2.off()
    coil_B_1.off()
    coil_B_2.on()
    sleep(time_delay)

    # step 1
    coil_A_1.on()
    coil_A_2.off()
    coil_B_1.on()
    coil_B_2.off()
    sleep(time_delay)

    # step 2
    coil_A_1.off()
    coil_A_2.on()
    coil_B_1.on()
    coil_B_2.off()
    sleep(time_delay)

    coil_A_1.off()
    coil_A_2.off()
    coil_B_1.off()
    coil_B_2.off()

def hold_motor():
# hold motor steady
    coil_A_1.on()
    coil_A_2.off()
    coil_B_1.on()
    coil_B_2.off()

for _ in range(10):
    step_backwards()
    print("im running backwards")
        
sleep(1)
for _ in range(10):
    step_forward()
    print("im running forwards")
sleep(1)   

while True:
    hold_motor()
    servo_cmd()
    sleep(1)



# def return_home():
# # run forwards untill limit switch is pressed 
#     while button_cmd(limit) = false:
#         step_forward()

#     step_backwards(5)   # then run backwards x number of steps
    
# def rps_position():

#     match symbol:
#     case "rock":
#          action-1
#     case "paper":
#          action-2
#     case "scissor":
#          action-3
#     case _:
#         return_home()
    
# print("im done")




