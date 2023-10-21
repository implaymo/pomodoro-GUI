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


# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    count_down(5 * 60)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    """Count down timer"""
    # Transforms time into minutes and seconds
    count_min = math.floor(count/60)
    count_sec = count % 60
    # Setups timer to work like 00:00
    canvas.itemconfig(timer, text=f"{count_min:02}:{count_sec:02}")
    # Decreases time in timer
    if count > 0:
        root.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #

# Window
root = Tk()
root.title("Pomodoro timer")
root.config(padx=100, pady=50, bg=PINK)

# Image setup
canvas = Canvas(root, width=400, height=500, bg=PINK, highlightthickness=0)
canvas.grid(column=2, row=2, rowspan=2)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(200, 250, image=tomato_img)

# Text
timer = canvas.create_text(200, 250, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
timer_text = canvas.create_text(200, 100, text="TIMER", fill=GREEN, font=(FONT_NAME, 50, "bold"))
check_mark = canvas.create_text(200, 400, text="✔️", fill=GREEN, font=(FONT_NAME, 10, "bold"))

# Start button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=1, row=3)
# Reset button
reset_button = Button(text="Reset")
reset_button.grid(column=3, row=3)


root.mainloop()
