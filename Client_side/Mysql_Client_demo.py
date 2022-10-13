from sqlite3 import Cursor
from XInput import *
import os
import mysql.connector
import time

class Client_Demo:
    def __init__(self):
        self.DB = ""

        #Connect to the mysql database
        self.Connect_mysql();

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

                        self.Writing_mysql("1");

                    #Detecting value for backward movment
                    elif(event.y <= -0.9900000):
                        print("Backward")
                        time.sleep(.45)
                        self.Writing_mysql("2")

                    #LEFT AND RIGHT MOVEMENT HAPPEND IN THE X-AXIS 
                    #IF THE VALUE IS POSITIVE THE THIS MEANS MOVE RIGHT
                    #IF THE VALUE IS NEGATIVE THE THIS MEANS MOVE LEFT 
                    elif(event.x >= 0.95000000):
                        print("Right")
                        time.sleep(.45)
                        self.Writing_mysql("3")
                    elif(event.x <= -0.95000000):
                        print("Left")
                        time.sleep(.45)
                        self.Writing_mysql("4")
            
            #Command's from user
            elif (event.type == EVENT_BUTTON_PRESSED):
                if(event.button == "BACK"):
                    print("Closing program")
                    exit()

    #Creating a connection to mysql database
    def Connect_mysql(self):
        self.DB = mysql.connector.connect(
            host="192.168.0.8",
            user="WinApp",
            password="dinero0123",
            database="robot"
        );

    #Writing value to the table
    def Writing_mysql(self, value):
        Cursor = self.DB.cursor()

        Cursor.execute(" Delete from Movement;")

        sql = """ INSERT INTO Movement(ID, value) VALUES  (%s,%s) """;
        values = (0,value)
        #Write the movement value
        Cursor.execute(sql, values);
        self.DB.commit()

       # self.DB.close()
        


Client_Demo();
