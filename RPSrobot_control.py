from gpiozero import Button
from time import sleep
from RPSrobot import LEDController  
from RPSrobot import ButtonController 
from RPSrobot import LCD
from RPSrobot import StepperMotorController
from RPSrobot import ServoController
from handTracking import HandDetector

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

# Instantiate component controllers
servo_l = ServoController(16)
servo_r = ServoController(12)
stepper_motor= StepperMotorController(stepper_motor_pins)

# leds = LEDController([10, 9, 11])
# Define the pin mappings for each LED color
led_pin_mapping = {
    "green": 10,
    "amber": 9,
    "red": 11
}
# buttons = ButtonController([4, 5, 6, 13])
button_pin_mapping = {
    "limit": 4,
    "start": 5,
    "stop": 6,
    "reset": 13
}

# Create an instance of the LEDController class
led_controller = LEDController(led_pin_mapping)

# Create an instance of the ButtonController class
button_controller = ButtonController(button_pin_mapping)

lcd = LCD(rs=17, enable=18, d4=2, d5=3, d6=24, d7=25)  # Assign GPIO 2 to D4 and GPIO 3 to D5


# Main control program

def start_game():
    # Set score to zero for human and bot
    human_score = 0
    bot_score = 0
    
    lcd.clear()
    lcd.write_message("Let's play")


while not button_controller.buttons["stop"].is_pressed:
    if button_controller.buttons["start"].is_pressed:
        start_game()
    elif button_controller.buttons["reset"].is_pressed:
        start_game()

try:
    while True:
        
        # button_controller.wait_for_press("start")
        servo_l.set_position(1)
        
        # for _ in range(10):
        #     stepper_motor.step_forward()
            
        # sleep(1)
        # stepper_motor_b.step_forward()
        # led_controller.turn_on("green")
        # buttons.wait_for_press("limit")
        # led_controller.turn_off("green")
except KeyboardInterrupt:
    pass