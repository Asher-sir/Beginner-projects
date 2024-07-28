from tkinter import Tk
from tkinter import Label
import winsound
import time
row=Tk()
def show_time():
    clock=time.strftime("%I:%M:%S %p")
    background.config(text=clock)
    background.after(400,show_time)





row.title("Clock")
winsound.Beep(440, 1000)
background=Label(row,font=("arial",190),bg="black",fg="white")
background.pack()
show_time()
row.mainloop()


