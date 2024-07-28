import time#importing the modules 
import winsound

sec=int(input("enter the timer in seconds"))
"""taking input you take input for hours,mins,secs differently
#but i just took it once"""

for i in range(sec,0,-1):
    timer=i
    seconds=i%60
    minutes=int(i / 60)%60
    hours= int(i/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)#the program keeps on repeating after one sec

print("times up")
winsound.Beep(740,1000)#wanted to put beep from previous project brrrr