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

        self.address = (("127.0.0.1", 100))
        self.s = ""
        self.message =""
        
    
        if(self.Remote_detection()):
            print ("waiting to connect to server")
            
            #Declare socket
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #connect to server
            self.s.connect(self.address);
            print("Connect to server")
            
            while True:
                
                self.joystic_movement()

        else:
            print("No Remote detected (Please connect device) ")
            exit();

#   This function detects if a remote is connected
    def Remote_detection(self):
        self.events = get_events();
        for event in self.events:
            if (event.type == EVENT_CONNECTED):
                print("Xbox Remote Connected ")
                return True

            elif (event.type == EVENT_DISCONNECTED):
                print("Please connect the device")
                exit()



# This function detects if the joystic has move
    def joystic_movement(self):
        self.events = get_events()
        for event in self.events:
            if(event.type == EVENT_STICK_MOVED):
                if(event.stick == LEFT):
                    #Forward
                    if (event.y >= 0.95):
                        self.message= "1"
                        print("Forward")
                        self.Send_MSG()

                    if (event.x >= 0.95):
                        self.message = "2"
                        print("Rigth")
                        self.Send_MSG()

                    if(event.x <= -0.95):
                        self.message = "3"
                        print("Left")
                        self.Send_MSG()
                    
                    if(event.y <= -0.95):
                        self.message = "4"
                        print("Backward")
                        self.Send_MSG()

            elif(event.type == EVENT_BUTTON_PRESSED):
                if(event.button == "BACK"):
                    print("Closing program")
                    #SEND MESSAGE TO SERVER TO INFORM OF CLOSING
                    self.message = "c"
                    self.Send_MSG();
                    self.s.close()
                    exit()



#Send message to the server
    def Send_MSG(self):
        self.s.send(self.message.encode('utf-8'));
        self.message = ""

                    
Client();
