from XInput import *
import os


set_deadzone(DEADZONE_TRIGGER,10)


while 1:
    events = get_events()
    for event in events:

        #if the remote device connected print 
        if (event.type == EVENT_CONNECTED):
            print("Xbox Remote Connected")

        elif (event.type == EVENT_DISCONNECTED):
            exit()

            #getting movement from stick
        elif(event.type == EVENT_STICK_MOVED):
            if(event.stick == LEFT):
                print(" Left_Thumb_x: " + str(event.x) + " " + " Left_thumb_y: " + str(event.y))


            
            elif (event.stick == RIGHT):                
                print(" Right_Thumb_x: " + str(event.x) + " " + " Right_thumb_y: " + str(event.y))
        
        elif (event.type == EVENT_BUTTON_PRESSED):
        
            if(event.button == "START"):
                print("Connection status")

        #Remote exit
            if(event.button == "BACK"):
                print("Exit")
                exit()