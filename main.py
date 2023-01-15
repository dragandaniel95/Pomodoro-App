import tkinter
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


def reset_time():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
    label_checkmark.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12, "bold"))


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="Break", bg=YELLOW, fg=RED, font=(FONT_NAME, 35, "bold"))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_timer.config(text="Break", bg=YELLOW, fg=PINK, font=(FONT_NAME, 35, "bold"))
    else:
        count_down(work_sec)
        label_timer.config(text="Work", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  # Editeaza text-ul unui Canvas
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        label_checkmark.config(text=mark)
# ---------------------------- UI SETUP -------------------------------#


# Window Create
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Canvas Create (pentru a importa o imagine si a scrie peste ea)
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Label - Timer
label_timer = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
label_timer.grid(column=1, row=0)

# Label - Checkmark
label_checkmark = tkinter.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12, "bold"))
label_checkmark.grid(column=1, row=3)

# Start Button
start_button = tkinter.Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

# Reset Button
start_button = tkinter.Button(text="Reset", command=reset_time)
start_button.grid(column=2, row=2)

window.mainloop()
