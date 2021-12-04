PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
from tkinter import *
import datetime
window= Tk()
def endcount():
    window.after_cancel(timer)
    canva.itemconfig(count_text, text='00:00')
    title.config(text="Stop")
def startcount():
    global reps
    reps+=1
    print(reps)
    workmin=WORK_MIN*60
    short_brakr=SHORT_BREAK_MIN*60
    long_brake=LONG_BREAK_MIN*60
    if reps % 8==0:
        title.config(text="Long Brake")
        count_down(long_brake)
    elif reps % 2==0:
        title.config(text="Short Brake")
        count_down(short_brakr)
    else:
        title.config(text="Working ")
        count_down(workmin)


def count_down(count):
    global timer
    time=datetime.timedelta(seconds=count)
    canva.itemconfig(count_text, text=time)
    if count >0:
        timer=window.after(1000,count_down,count-1)
    else:
        startcount()
window.title('Pomodoro ')
window.config(bg=YELLOW, )
canva=Canvas(window, width=500, height=400, bg=YELLOW, highlightthickness=0)
title=Label(text="Timer", font=(FONT_NAME,35,'bold'), fg=GREEN,bg=YELLOW)
title.place(x=200,y=30)
canva.pack()

image=PhotoImage(file='tomato.png', )
canva.create_image(150, 80, anchor=NW, image=image)
count_text=canva.create_text(250,200,text='00:00',fil='#fff',font=(FONT_NAME,35, 'bold'))

start=Button(text="start" ,command=startcount)
end=Button(text="End" ,command=endcount)
start.place(x=130, y=320)
end.place(x=350, y=320)

window.mainloop()