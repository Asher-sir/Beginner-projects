from tkinter import Tk#importing the various modules
from tkinter import Label
import winsound
import time
row=Tk()
def show_time():
    clock=time.strftime("%I:%M:%S %p")#this would show the current time
    background.config(text=clock)
    background.after(400,show_time)#this refreshes the time after 400 miliseconds why (why not)





row.title("Clock")
winsound.Beep(440, 1000)#beeepppp sound go brrrrr
background=Label(row,font=("arial",190),bg="black",fg="white")
background.pack()
show_time()
row.mainloop()


