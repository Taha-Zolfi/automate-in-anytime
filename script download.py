from datetime import datetime
import time
import pyautogui

alarm_time = input("Enter script run Time (HH:MM:SS)\n")

alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_second = alarm_time[6:8]

print("waiting till that time...")

now = datetime.now()


c = 277

distance = 200
while True:
    now = datetime.now()


    c_hour = now.strftime("%H")
    c_minute = now.strftime("%M")
    c_second = now.strftime("%S")    


    if alarm_hour == c_hour:
            if alarm_minute == c_minute:
                if alarm_second == c_second:
#---------------learn pyautogui and come back to write your code------------                    
                    for i in range(11):

                        pyautogui.click(957,c)
                        time.sleep(0.5)
                        pyautogui.click(711,528)
                        time.sleep(0.5)
                        pyautogui.click(412,15)

                        c+=40
                                          
#---------------learn pyautogui and come back to write your code------------                        
                    break
