from tkinter import *

screen = Tk()
screen.attributes('-fullscreen', True)
screen.configure(bg="#3f3f3f")

# Get actual screen size
screen_width = screen.winfo_screenwidth()
screen_height = screen.winfo_screenheight()

# Create a canvas that fills the screen
canvas = Canvas(screen, width=screen_width, height=screen_height, bg="#3f3f3f", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Center point
cx = screen_width // 2
cy = screen_height // 2


# Gear
gear = Label(screen, font=("Impact", 250), text="N", fg="white", bg="#3f3f3f")
canvas.create_window(cx, cy, window=gear)
gear_label = Label(screen, font=("Impact", 60), text="Gear", bg="#3f3f3f", fg="white")
canvas.create_window(cx, cy + 160, window=gear_label)

# RPM
rpm = Label(screen, font=("Impact", 100), text="00000", fg="white", bg="#3f3f3f")
canvas.create_window(cx, cy - 300, window=rpm)
rpm_label = Label(screen, font=("Impact", 30), text="RPM", fg="white", bg="#3f3f3f")
canvas.create_window(cx, cy - 210, window=rpm_label)

# Speed
speed = Label(screen, font=("Impact", 100), text="000", fg="white", bg="#3f3f3f")
canvas.create_window(cx, cy + 280, window=speed)
speed_label = Label(screen, font=("Impact", 30), text="km/h", fg="white", bg="#3f3f3f")
canvas.create_window(cx, cy + 370, window=speed_label)

# Lap Number
lap = Label(screen, font=("Impact", 70), text="00", fg="black")
canvas.create_window(cx-530, cy-330, window=lap)
lap_label = Label(screen, font=("Impact", 30), text="Lap", fg="white", bg="#3f3f3f")
canvas.create_window(cx-530, cy-230, window=lap_label)

# Position
pos = Label(screen, font=("Impact", 70), text="00", fg="black")
canvas.create_window(cx-700, cy-330, window=pos)
pos_label = Label(screen, font=("Impact", 30), text="POS", fg="white", bg="#3f3f3f")
canvas.create_window(cx-700, cy-230, window=pos_label)

# Current Lap
current_lap_label = Label(screen, font=("Impact", 50), text="Current lap", fg="white", bg="#3f3f3f")
canvas.create_window(cx-770, cy, window=current_lap_label)

def exit_fullscreen(event):
    screen.attributes("-fullscreen", False)
    print("workssss")

def enter_fullscreen(event):
    screen.attributes("-fullscreen", True)
screen.bind("<Escape>", exit_fullscreen)
screen.bind("<F11>", enter_fullscreen)


screen.mainloop()
