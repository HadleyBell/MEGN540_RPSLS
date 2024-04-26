import gpiod

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
red_LED = chip.get_line(RED_LED_PIN)
ylw_LED = chip.get_line(YLW_LED_PIN)
grn_LED = chip.get_line(GRN_LED_PIN)
limit = chip.get_line(LIMIT_PIN)

# Define GPIO pins as input or output
blk_button.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)
red_button.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)
grn_button.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)
red_LED.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
ylw_LED.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
grn_LED.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
limit.request(consumer="Limit", type=gpiod.LINE_REQ_DIR_IN)

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
        print ("Red button was pushed")
        ylw_LED.set_value(1)
       elif grn_button_state == 1:
        print ("Green button was pushed")
        red_LED.set_value(1)
       elif limit_state == 0:
        print ("LIMIT REACHED!!")
        red_LED.set_value(1)
       else:
        print("No button pushed")
        grn_LED.set_value(0)
        ylw_LED.set_value(0)
        red_LED.set_value(0)
finally:
    blk_button.release()
    red_button.release()
    grn_button.release()