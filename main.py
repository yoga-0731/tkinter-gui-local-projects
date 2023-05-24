import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer_cycle = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer_cycle
    timer_cycle = 0
    window.after_cancel(timer)
    timer_label.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global timer_cycle
    timer_cycle += 1
    if timer_cycle % 8 == 0:
        timer_label.config(text='Break!', fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif timer_cycle % 2 == 0:
        timer_label.config(text='Break!', fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text='Work!', fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minute = math.floor(count / 60)
    count_second = count % 60
    if count_second < 10:
        count_second = f"0{count_second}"  # Dynamic Typing (count_sec previously had int, now has str)
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(timer_cycle/2)):
            mark += "✔"
        checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title('Pomodoro')

timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, 'bold'))
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # The image's width and height
tomato = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato)  # Half of image's width and height
timer_text = canvas.create_text(102, 130, text="00:00", fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(row=1, column=1)

start_button = Button(text='Start', bg='white', command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', bg='white', command=reset_timer)
reset_button.grid(row=2, column=2)

checkmark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, 'bold'))
checkmark.grid(row=3, column=1)

window.mainloop()
