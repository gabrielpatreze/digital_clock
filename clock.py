from tkinter import *
from tkinter.ttk import *
import pytz
from datetime import datetime
from time import strftime


root = Tk()

root.title('Relógio Digital')

def clock():
    tick = strftime('%H:%M:%S %p')

    label.config(text = tick)
    label.after(1000, clock)

label = Label(root, font=('sans', 50), background = 'navy', foreground = 'white')

label.pack(anchor = 'center')

clock()
mainloop()
