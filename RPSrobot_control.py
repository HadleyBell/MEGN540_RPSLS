from gpiozero import Button
from time import sleep
from RPSrobot import LEDController  
from RPSrobot import ButtonController 
from RPSrobot import LCD
from RPSrobot import StepperMotorController
from handTracking import HandDetector
from ServoSerialTest import ServoSerial
import serial, time
import gpiod
import math
import cv2
import mediapipe as mp
import random
#import I2C_LCD_driver

# While stop button is not pressed 
    # When start button is pressed
        # set score to zero for human and bot
        # start videocapture
        # call hand tracking
        # put arm in "home position"
        # LCD display "lets play"
        # LEDs 3, 2, 1, go
        # detect hand shape
        # stop video capture
        
        # robot also throws signal randomly
        # increment score for appropriate player
        # score displayed "Bot:1 Human:0"
        
     # When re-start button is pressed
        # reset score to zeros     

stepper_motor_pins = [23, 24, 27, 22]  
# button_pins = [4, 19, 26, 13]
# GPIO pin definitions
BLK_BUTTON_PIN = 13
RED_BUTTON_PIN = 26
GRN_BUTTON_PIN = 19

RED_LED_PIN = 10
YLW_LED_PIN = 9
GRN_LED_PIN = 11
LIMIT_PIN = 4  

chip = gpiod.Chip('gpiochip4')

# Access GPIO pins on PI
blk_button = chip.get_line(BLK_BUTTON_PIN)
red_button = chip.get_line(RED_BUTTON_PIN)
grn_button = chip.get_line(GRN_BUTTON_PIN)
limit = chip.get_line(LIMIT_PIN)

red_LED = chip.get_line(RED_LED_PIN)
ylw_LED = chip.get_line(YLW_LED_PIN)
grn_LED = chip.get_line(GRN_LED_PIN)


# Define GPIO pins as input or output
blk_button.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)
red_button.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)
grn_button.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)
limit.request(consumer="Limit", type=gpiod.LINE_REQ_DIR_IN)

red_LED.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
ylw_LED.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
grn_LED.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)

# Instantiate component controllers
stepper_motor= StepperMotorController(stepper_motor_pins)

# leds = LEDController([10, 9, 11])
# Define the pin mappings for each LED color
# led_pin_mapping = {
#     "green": 10,
#     "amber": 9,
#     "red": 11
# }


# # Create an instance of the LEDController class
# led_controller = LEDController(led_pin_mapping)

# Create an instance of the ButtonController class
# button_controller = ButtonController()

servo = ServoSerial()

# lcd = LCD(rs=17, enable=18, d4=2, d5=3, d6=24, d7=25)  # Assign GPIO 2 to D4 and GPIO 3 to D5



def random_char():
   char_list = ["R", "P", "S"]
   return random.choice(char_list)
   

def start_game():
    # Set score to zero for human and bot
    human_score = 0
    bot_score = 0
    sleep(0.1)
    servo.set_position("X")
    sleep(0.5)

    for _ in range(5):
        stepper_motor.step_backwards()
    sleep(.25)
    limit_state = limit.get_value()
    while limit_state == 0:
        stepper_motor.step_forward()
        limit_state = limit.get_value()
    for _ in range(60):
        stepper_motor.step_backwards()
    sleep(2)
        
    # lcd.clear()
    # lcd.write_message("Let's play")

def get_hand_position(cap):
    # 2 for external camera connected to computer, 0 built-in camera

    # Initialize the HandDetector class
    detector = HandDetector(staticMode=False, maxHands=1)

    for _ in range(10):
        success, img = cap.read()

        # Find hands in the current frame
        # The 'draw' parameter draws landmarks and hand outlines on the image if set to True
        # The 'flipType' parameter flips the image, making it easier for some detections
        hands, img = detector.findHands(img, draw=True, flipType=True)

        # Check if any hands are detected
        if hands:

            hand1 = hands[0]  # Get the first hand detected
            lmList1 = hand1["lmList"]  # List of 21 landmarks for the first hand
            bbox1 = hand1["bbox"]  # Bounding box around the first hand (x,y,w,h coordinates)
            center1 = hand1['center']  # Center coordinates of the first hand
            handType1 = hand1["type"]  # Type of the first hand ("Left" or "Right")

            # Count the number of fingers up for the first hand
            fingers1 = detector.fingersUp(hand1)
            # print(f'H1 = {fingers1.count(1)}', end=" ")  # Print the count of fingers that are up

            # Calculate distance between specific landmarks on the first hand and draw it on the image
            length, info, img = detector.findDistance(lmList1[8][0:2], lmList1[12][0:2], img, color=(255, 0, 255),scale=10)

            if fingers1.count(1) == 0:
                signal = "rock"
                print('Rock', end = " ")
            elif (length >= 65 or fingers1.count(1) == 2):
                signal = "scissors"
                print('Scissors', end = " ")
            elif fingers1.count(1) == 4 or fingers1.count(1) == 5:
                print('Paper', end = " ")
                signal = "paper"
            else:
                print(f'H1 = {fingers1.count(1)}', end=" ")
                signal = "unknown"
            
        return(signal)

def throw():
    # servo.set_position("P")
    # time.sleep(1.25)
    # servo.set_position("S")
    # time.sleep(1.25)
    # servo.set_position("X")

    for _ in range(45):
        stepper_motor.step_forward()
    
    throw = random_char()
    print(throw)
    servo.set_position(throw)
    time.sleep(2)
   

# Main control program

# while True:
#     # not button_controller.buttons["stop"].is_pressed:
#     if button_controller.buttons["start"].is_pressed:
#         print("button pressed")
#         start_game()
#         print("started")
#     elif button_controller.buttons["reset"].is_pressed:
#         start_game()

# while True:
#     # not button_controller.buttons["stop"].is_pressed:
#     if grn_button_state == 1:
#         print("button pressed")
#         start_game()
#         print("started")
#     elif button_controller.buttons["reset"].is_pressed:
#         start_game()


# for _ in range(10):
#     stepper_motor.step_forward()

# try:
#     while True:
        
#         # button_controller.wait_for_press("start")
        

            
#         # sleep(1)
#         # stepper_motor_b.step_forward()
#         # led_controller.turn_on("green")
#         # buttons.wait_for_press("limit")
#         # led_controller.turn_off("green")
# except KeyboardInterrupt:
#     pass

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()



try:
   while True:
       blk_button_state = blk_button.get_value()
       red_button_state = red_button.get_value()
       grn_button_state = grn_button.get_value()
       limit_state = limit.get_value()
       
       if blk_button_state == 1:
        print("Black button was pushed")
        grn_LED.set_value(1)
       elif red_button_state == 1:
            servo.set_position("P")
            time.sleep(1.25)
            servo.set_position("S")
            time.sleep(1.25)
            servo.set_position("R")
            ylw_LED.set_value(1)
       elif grn_button_state == 1:
            start_game()
            throw()
       elif limit_state == 1:
        print ("LIMIT REACHED!!")
        red_LED.set_value(1)
       else:
        grn_LED.set_value(0)
        ylw_LED.set_value(0)
        red_LED.set_value(0)
finally:
    blk_button.release()
    red_button.release()
    grn_button.release()


# try:
#     while True:
#         blk_button_state = blk_button.get_value()
#         red_button_state = red_button.get_value()
#         grn_button_state = grn_button.get_value()
#         limit_state = limit.get_value()
       
#         if blk_button_state == 1:
#             hand = get_hand_position(cap)
#             print(hand)
        
#         elif red_button_state == 1:
#             servo.set_position("P")
#             time.sleep(1.25)
#             servo.set_position("S")
#             time.sleep(1.25)
#             servo.set_position("X")
#             ylw_LED.set_value(1)
#         elif grn_button_state == 1:
#             start_game()
#             throw()
#         elif limit_state == 1:
# finally:
#  blk_button.release()
#  red_button.release()
#  grn_button.release()