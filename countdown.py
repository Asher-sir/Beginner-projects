import time
import winsound

sec=int(input("enter the timer in seconds"))

for i in range(sec,0,-1):
    timer=i
    seconds=i%60
    minutes=int(i / 60)%60
    hours= int(i/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("times up")
winsound.Beep(740,1000)