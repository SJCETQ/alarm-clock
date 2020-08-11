


# Importing all the necessary libraries to form the alarm clock:
from tkinter import *
import datetime
import time
import winsound


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:", date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break


def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)


clock = Tk()
clock.title("Sanjay Yadav -  Alarm Clock")
# clock.iconbitmap(r"dataflair-logo.ico")
clock.geometry("400x300")
time_format = Label(clock, text="Enter time in 24 hour format!", fg="blue", bg="yellow", font="Arial").place(x=100, y=100)
addTime = Label(clock, text="Hour  Min   Sec", font=80).place(x=150, y=20)
setYourAlarm = Label(clock, text="When to wake you up", fg="red", relief="sunken",
                     font=("Helevetica", 12, "bold")).place(x=120, y=150)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

# Time required to set the alarm clock:
hourTime = Entry(clock, textvariable=hour, bg="pink", fg="white", width=10).place(x=100, y=55)
minTime = Entry(clock, textvariable=min, bg="pink", fg="white", width=10).place(x=150, y=55)
secTime = Entry(clock, textvariable=sec, bg="pink", fg="white", width=10).place(x=210, y=55)

# To take the time input by user:
submit = Button(clock, text="Set Alarm", bg="blue", fg="white", width=30, command=actual_time).place(x=100, y=190)

clock.mainloop()
# Execution of the window.
