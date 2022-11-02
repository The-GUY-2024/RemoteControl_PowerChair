from asyncio import events
import os
import socket
import sys
from XInput import *


class Client:
    def __init__(self):
        #Remote parameters 
        set_deadzone(DEADZONE_TRIGGER, 10)
        self.events = ""

        self.address = ("192.168.0.7", 100)
        self.s = ""
        

        while 1:
            self.Remote_detection()

    def Remote_detection(self):
        self.events = get_events();
        for event in self.events:
            if (event.type == EVENT_CONNECTED):
                print("Xbox Remote Connected ")
            
            elif (event.type == EVENT_DISCONNECTED):
                print("Please connect the device")
                exit()
