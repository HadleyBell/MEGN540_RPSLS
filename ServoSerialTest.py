#!/usr/bin/env python
# -*- coding: utf-8 -*-
# lsusb to check device name
#dmesg | grep "tty" to find port name

import serial, time


class ServoSerial:

    # def __init__(self):
    #     self.serial_port =  serial.Serial("/dev/ttyACM0", 9600, timeout=1 )
    #     time.sleep(0.1)
    #     print("Serial Started")
    #     if self.serial_port.isOpen():
    #         print("{} connected!".format(self.serial_port.port))
    def set_position(self, position):
        self.serial_port =  serial.Serial("/dev/ttyACM0", 9600, timeout=1 )
        time.sleep(0.1)
        if self.serial_port.isOpen():
            self.serial_port.write(position.encode())
        # while self.serial_port.inWaiting()==0: pass
        # if  self.serial_port.inWaiting()>0: 
        #     answer=self.serial_port.readline()
        #     self.serial_port.flushInput() #remove data after reading

