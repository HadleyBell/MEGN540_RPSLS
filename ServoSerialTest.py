#!/usr/bin/env python
# -*- coding: utf-8 -*-
# lsusb to check device name
#dmesg | grep "tty" to find port name

import serial, time


class ServoSerial:

   # def __init__(self, baudrate = 9600, timeout =1 ):
    #    # self.serial_port =  serial.Serial("/dev/ttyACM0", baudrate, timeout=timeout )
    #     time.sleep(0.1)
    #     if self.serial_port.isOpen():
    #         print("{} connected!".format(self.serial_port.port))

    def set_position(self, position):
        self.serial_port =  serial.Serial("/dev/ttyACM0", 9600, timeout=1 )
        if self.serial_port.isOpen():
            self.serial_port.write(position.encode())

    # def demo(self):
    #     self.set_position("R")
    #     time.sleep(1.25)
    #     self.set_position("P")
    #     time.sleep(1.25)
    #     self.set_position("S")
    #     time.sleep(1.25)
    #     self.set_position("X")



# servo = ServoSerial()

# # DEMO
# servo.set_position("R")
# time.sleep(1.25)
# servo.set_position("P")
# time.sleep(1.25)
# servo.set_position("S")
# time.sleep(1.25)
# servo.set_position("X")

