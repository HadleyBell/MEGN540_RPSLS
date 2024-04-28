from gpiozero import Servo, Motor, LED, Button, OutputDevice
from time import sleep

class StepperMotorController:
    def __init__(self, pins, time_delay=0.007):
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

        self.coil_A_1.off()
        self.coil_A_2.off()
        self.coil_B_1.off()
        self.coil_B_2.off()


    def step_backwards(self):
        
        # step 3
        self.coil_A_1.off()
        self.coil_A_2.on()
        self.coil_B_1.off()
        self.coil_B_2.on()
        sleep(self.time_delay)
        
        # step 4
        self.coil_A_1.on()
        self.coil_A_2.off()
        self.coil_B_1.off()
        self.coil_B_2.on()
        sleep(self.time_delay)
        
        # step 1
        self.coil_A_1.on()
        self.coil_A_2.off()
        self.coil_B_1.on()
        self.coil_B_2.off()
        sleep(self.time_delay)

        # step 2
        self.coil_A_1.off()
        self.coil_A_2.on()
        self.coil_B_1.on()
        self.coil_B_2.off()
        sleep(self.time_delay)

        self.coil_A_1.off()
        self.coil_A_2.off()
        self.coil_B_1.off()
        self.coil_B_2.off()

    def stop_motor(self):
        self.coil_A_1.off()
        self.coil_A_2.off()
        self.coil_B_1.off()
        self.coil_B_2.off()

    def hold_motor(self):
        # Hold motor steady
        self.coil_A_1.on()
        self.coil_A_2.off()
        self.coil_B_1.on()
        self.coil_B_2.off()
        
class LCD:
    def __init__(self, register, enable, d4, d5, d6, d7):
        self.register = OutputDevice(register)
        self.enable = OutputDevice(enable)
        self.data_pins = [OutputDevice(pin) for pin in [d4, d5, d6, d7]]

        # Initialize the LCD
        self.command(0x33)
        self.command(0x32)
        self.command(0x28)  # 4-bit mode, 2 lines, 5x7 font
        self.command(0x0C)  # Display on, cursor off, blink off
        self.command(0x06)  # Increment cursor

    def command(self, bits, mode=0):
        self.register.value = mode
        self.enable.value = True

        for i in range(4):
            self.data_pins[i].value = (bits >> i) & 1

        self.enable.value = False
        self.enable.value = True

    def clear(self):
        self.command(0x01)  # Clear display

    def write_message(self, message):
        for char in message:
            self.command(ord(char), mode=1)  # Write character


class LEDController:
    def __init__(self, led_pin_mapping):
        self.leds = {color: LED(pin) for color, pin in led_pin_mapping.items()}

    def turn_on(self, color):
        if color in self.leds:
            self.leds[color].on()

    def turn_off(self, color):
        if color in self.leds:
            self.leds[color].off()

class ButtonController:
    def __init__(self, pins):
        self.limit = Button(pins[0])
        self.start = Button(pins[1])
        self.stop = Button(pins[2])
        self.reset = Button(pins[3])

    # self.buttons = {action: Button(pin) for action, pin in button_pin_mapping.items()}
    # buttons = ButtonController([4, 5, 6, 13])
    # button_pin_mapping = {
    #     "limit": 4,
    #     "start": 19,
    #     "stop": 26,
    #     "reset": 13
    # }

    def wait_for_press(self, action):
        self.buttons = {"limit": 4,"start": 19,"stop": 26,"reset": 13}
        self.buttons[action].is_pressed()
            


    
    