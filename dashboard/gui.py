from tkinter import *

screen = Tk()
screen.geometry("1920x1080")
screen.title("FM7 Dashboard")
screen.configure(bg="#3f3f3f")
screen.attributes('-fullscreen', True)
canvas = Canvas(screen, width=1920, height=1080, bg="#3f3f3f", highlightthickness=0)
canvas.pack(fill="both", expand=True)


gear = Label(screen, font=("Impact", 250), text="N", fg="white", bg="#3f3f3f")
canvas.create_window(960, 540, window=gear)
gear_label = Label(screen, font=("Impact", 60), text="Gear", bg="#3f3f3f", fg="white", anchor= "center")
canvas.create_window(960, 700, window=gear_label)

rpm = Label(screen, font=("Impact", 100), text="00000", fg="white", bg="#3f3f3f")
canvas.create_window(960, 240, window=rpm)
rpm_label = Label(screen, font=("Impact", 30), text="RPM", fg="white", bg="#3f3f3f")
canvas.create_window(960, 330, window=rpm_label)

speed = Label(screen, font=("Impact", 100), text="000", fg="white", bg="#3f3f3f")
canvas.create_window(960, 840, window=speed)
speed_label = Label(screen, font=("Impact", 30), text="km/h", fg="white", bg="#3f3f3f")
canvas.create_window(960, 925, window=speed_label)








def exit_fullscreen(event):
    screen.attributes("-fullscreen", False)

screen.bind("<Escape>", exit_fullscreen)
screen.mainloop()