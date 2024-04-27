# While stop button is not pressed 
    # When start button is pressed
        # start videocapture
        # put arm in "home position"
        # LCD display "lets play"
        # LEDs 3, 2, 1, go
        
        # user gives signal
        # robot also throws signal randomly
        # score is calculated 
        # score displayed "Bot:1 Human:0"
        
     # When re-start button is pressed
        # reset score
        # keep playing
        
        
from gpiozero import Servo, Motor, LED, Button, OutputDevice
from time import sleep

stepper_motor_pins = [23, 24, 27, 22]

class ServoController:
    def __init__(self, pin):
        self.servo = Servo(pin)

    def set_position(self, position):
        self.servo.value = position

class StepperMotorController:
    def __init__(self, pins, time_delay=0.005):
        self.coil_A_1 = OutputDevice(pins[0])
        self.coil_A_2 = OutputDevice(pins[1])
        self.coil_B_1 = OutputDevice(pins[2])
        self.coil_B_2 = OutputDevice(pins[3])
        self.time_delay = time_delay

    def step_forward(self):
        self.coil_A_1.on()
        self.coil_A_2.off()
        self.coil_B_1.on()
        self.coil_B_2.off()
        sleep(self.time_delay)

        self.coil_A_1.on()
        self.coil_A_2.off()
        self.coil_B_1.off()
        self.coil_B_2.on()
        sleep(self.time_delay)

        self.coil_A_1.off()
        self.coil_A_2.on()
        self.coil_B_1.off()
        self.coil_B_2.on()
        sleep(self.time_delay)

        self.coil_A_1.off()
        self.coil_A_2.on()
        self.coil_B_1.on()
        self.coil_B_2.off()
        sleep(self.time_delay)

    def step_backwards(self):
        # step 4
        self.coil_A_1.on()
        self.coil_A_2.off()
        self.coil_B_1.off()
        self.coil_B_2.on()
        sleep(self.time_delay)

        # step 3
        self.coil_A_1.off()
        self.coil_A_2.on()
        self.coil_B_1.off()
        self.coil_B_2.on()
        sleep(self.time_delay)

        # step 2
        self.coil_A_1.off()
        self.coil_A_2.on()
        self.coil_B_1.on()
        self.coil_B_2.off()
        sleep(self.time_delay)

        # step 1
        self.coil_A_1.on()
        self.coil_A_2.off()
        self.coil_B_1.on()
        self.coil_B_2.off()
        sleep(self.time_delay)

    def hold_motor(self):
        # Hold motor steady
        self.coil_A_1.on()
        self.coil_A_2.on()
        self.coil_B_1.on()
        self.coil_B_2.on()


class LEDController:
    def __init__(self, pin_mapping):
        self.leds = {color: LED(pin) for color, pin in pin_mapping.items()}

    def turn_on(self, color):
        if color in self.leds:
            self.leds[color].on()

    def turn_off(self, color):
        if color in self.leds:
            self.leds[color].off()

class ButtonController:
    def __init__(self, pins):
        self.buttons = [Button(pin) for pin in pins]

    def wait_for_press(self):
        for button in self.buttons:
            button.wait_for_press()
            
        

# Instantiate component controllers
servo_l = ServoController(16)
servo_r = ServoController(12)
stepper_motor= StepperMotorController(stepper_motor_pins)

leds = LEDController([10, 9, 11])
# Define the pin mappings for each LED color
led_pin_mapping = {
    "green": 10,
    "amber": 9,
    "red": 11
}
buttons = ButtonController([4, 5, 6, 13])

# Main control program
try:
    while True:

        # servo_l.set_position(0)
        # servo_r.set_position(1)
        
        for _ in range(10):
            stepper_motor.step_forward()
            
        # sleep(1)
        # stepper_motor_b.step_forward()
        leds.turn_on("green")
        buttons.wait_for_press()
        leds.turn_off(0)
except KeyboardInterrupt:
    pass

    
    