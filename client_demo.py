from XInput import *
import os
import mysql.connector
import time

class Client_Demo:
    def __init__(self):
        #Connect to the mysql database

        while True:
            
            self.Remote_input()

    def Remote_input(self):
        events = get_events()
        for event in events:


            if (event.type == EVENT_CONNECTED):
                print("Xbox Remote is connected ")

            elif (event.type == EVENT_DISCONNECTED):
                print ("closing this program")
                exit();


            # Stick movement  detection
            elif (event.type == EVENT_STICK_MOVED):
                if (event.stick == LEFT):
                    
                    #FORWARD AND BACKWARD MOVEMENT HAPPEND IN THE Y-AXIS 
                    #IF THE VALUE OF THE Y-AXIS IS POSSITIVE THE (COMMAND IS MOVE FORWARD)
                    #IF THE VALUE OF THE Y-AXIS IS NEGATIVE THE (COMMAND IS MOVE BACKWARD)

                    #Detect value for foward movement
                    if (float(event.y) >= float(0.900000)):
                        print("Forward")
                        time.sleep(.45)
                    
                    #Detecting value for backward movment
                    elif(event.y <= -0.9900000):
                        print("Backward")
                        time.sleep(.45)
                    
                    elif(event.x >= 0.95000000):
                        print("Right")
                        time.sleep(.45)

                    elif(event.x <= -0.95000000):
                        print("Left")
                        time.sleep(.45)
            
            #Command's from user
            elif (event.type == EVENT_BUTTON_PRESSED):
                if(event.button == "BACK"):
                    print("Closing program")
                    exit()

    #Creating a connection to mysql database
    def Connect_mysql(self):
        print()

Client_Demo();