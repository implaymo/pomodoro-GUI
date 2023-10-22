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
REPS = 0
TIMER_HEADER = "TIMER"
WORK_HEADER = "WORK"
BREAK_HEADER = "BREAK"
X_CHECK_MARK = 180
COUNTING = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    """RESETS TIMER"""
    global COUNTING
    check_mark_reset()
    canvas.itemconfig(timer, text="00:00")
    canvas.delete("clear_text")
    root.after_cancel(COUNTING)


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    """STARTS TIMER"""
    global REPS
    global X_CHECK_MARK
    work_time_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    # Checks which rep the timer is and switches the amount of time
    if REPS in [0, 2, 4, 6]:
        count_down(work_time_secs)
        canvas.itemconfig(timer_text, text=WORK_HEADER, fill=GREEN, font=(FONT_NAME, 50, "bold"))
        canvas.create_text(X_CHECK_MARK, 400, text="✔️", fill=GREEN,
                           font=(FONT_NAME, 10, "bold"), tags="clear_text")
        # Changes checkmark position
        X_CHECK_MARK += 20
    elif REPS in [1, 3, 5]:
        count_down(short_break_secs)
        canvas.itemconfig(timer_text, text=BREAK_HEADER, fill=PINK, font=(FONT_NAME, 50, "bold"))
    elif REPS in [7]:
        count_down(long_break_secs)
        canvas.itemconfig(timer_text, text=BREAK_HEADER, fill=RED, font=(FONT_NAME, 50, "bold"))
        # Clears checkmarks and changes position
        canvas.delete("clear_text")
        X_CHECK_MARK = 180
        REPS = -1
    REPS += 1

def check_mark_reset():
    """Resets checkmark position and reps"""
    global REPS
    global X_CHECK_MARK
    REPS = 0
    X_CHECK_MARK = 180

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(seconds):
    """Countdown time"""
    global COUNTING
    # Transforms time into minutes and seconds
    count_min = math.floor(seconds / 60)
    count_sec = seconds % 60
    # Setups timer to work like 00:00
    canvas.itemconfig(timer, text=f"{count_min:02}:{count_sec:02}")
    # Decreases time in timer
    if seconds > 0:
        COUNTING = root.after(1000, count_down, seconds - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

# Window
root = Tk()
root.title("Pomodoro timer")
root.config(padx=100, pady=50, bg=YELLOW)


# Image setup
canvas = Canvas(root, width=400, height=500, bg=YELLOW, highlightthickness=0)
canvas.grid(column=2, row=2, rowspan=2)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(200, 250, image=tomato_img)

# Text
timer = canvas.create_text(200, 250, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
timer_text = canvas.create_text(200, 100, text=TIMER_HEADER, fill=GREEN, font=(FONT_NAME, 50, "bold"))

# Start button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=1, row=3)

# Reset button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=3)

root.mainloop()
