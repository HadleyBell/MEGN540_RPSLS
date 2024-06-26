# LCD screen
# https://github.com/stechiez/raspberrypi_python/blob/main/lcd_16x2/lcd_16x2.py
    
import smbus
import time

# device parameters
I2C_ADDR = 0x27 #IC2 device address
LCD_WIDTH = 16 

# Device constants
LCD_CHR = 1     # Mode - Sending data
LCD_CMD = 0     # Mode - Sending command

# LCD Ram addresses
LCD_LINE_1 = 0x80
LCD_LINE_2 = 0xC0
LCD_LINE_3 = 0x94
LCD_LINE_4 = 0xD4

LCD_BLACKLIGHT = 0x08 #on
ENABLE = 0b000000100 # Enable bit

# Timing constatnts
E_PULSE = 0.0005
E_DELAY = 0.0005

# open i2c interface
bus = subus.SMBus(1)

def lcd_init():
    #initialize display
    lcd_byte(0x33, LCD_CMD) # 110011 Initialize
    lcd_byte(0x32, LCD_CMD) # 110010 Initialize
    lcd_byte(0x06, LCD_CMD) # 000110 Cursor move direction
    lcd_byte(0x0C, LCD_CMD) # Display on Cursor off, Blink off
    lcd_byte(0x28, LCD_CMD)# 101000 Data length, number of lines, font size
    lcd_byte(0x01, LCD_CMD) # 000001 clear display
    time.sleep(E_DELAY)

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = the data
  # mode = 1 for data
  #        0 for command

  bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT
  bits_low = mode | ((bits<<4) & 0xF0) | LCD_BACKLIGHT

  # High bits
  bus.write_byte(I2C_ADDR, bits_high)
  lcd_toggle_enable(bits_high)

  # Low bits
  bus.write_byte(I2C_ADDR, bits_low)
  lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
  # Toggle enable
  time.sleep(E_DELAY)
  bus.write_byte(I2C_ADDR, (bits | ENABLE))
  time.sleep(E_PULSE)
  bus.write_byte(I2C_ADDR,(bits & ~ENABLE))
  time.sleep(E_DELAY)

def lcd_string(message,line):
  # Send string to display

  message = message.ljust(LCD_WIDTH," ")

  lcd_byte(line, LCD_CMD)

  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)

def main():
  # Main program block

  # Initialise display
  lcd_init()

  while True:

    # Send some test
    lcd_string("RPi LCD tutorial",LCD_LINE_1)
    lcd_string("   STechiezDIY  ",LCD_LINE_2)

    time.sleep(3) # pauses then switches to the next string
  
    # Send some more text
    lcd_string("Subscribe to    ",LCD_LINE_1)
    lcd_string("     STechiezDIY",LCD_LINE_2)

    time.sleep(3) 

if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd_byte(0x01, LCD_CMD)