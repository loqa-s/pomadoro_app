from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    label_uppertext.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer_text, text='00:00')
    label_bottomtext.config(text='')
    button_start.config(state='normal')
    button_reset.config(state='disabled')
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    button_start.config(state='disabled')
    button_reset.config(state='normal')
    if reps % 2 != 0 and reps < 8:
        count_down(WORK_MIN * 60)
        label_uppertext.config(text='Work', fg=GREEN)
    elif reps % 2 == 0 and reps < 8:
        count_down(SHORT_BREAK_MIN * 60)
        label_uppertext.config(text='Break!', fg=PINK)
    else:
        count_down(LONG_BREAK_MIN * 60)
        label_uppertext.config(text='Break!', fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f'0{count_seconds}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_seconds}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += '✅'
        label_bottomtext.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomadoro!')
window.config(padx=100, pady=50, bg=YELLOW)

label_uppertext = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
label_uppertext.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

button_start = Button(text='Start', highlightthickness=0, highlightbackground=YELLOW, command=start_timer)
button_start.grid(column=0, row=2)

label_bottomtext = Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, 'bold'), pady=30)
label_bottomtext.grid(column=1, row=2)

button_reset = Button(text='Reset', highlightthickness=0,  highlightbackground=YELLOW, command=reset_timer, state='disabled')
button_reset.grid(column=2, row=2)

window.mainloop()
