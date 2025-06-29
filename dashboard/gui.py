import os
import math
from tkinter import *
from tkinter import font as tkFont
import ctypes
from PIL import Image, ImageTk
from dashboard.telemetry import GetIPAddr





def switch_to_dashboard():
    global selected_port, selected_game
    try:
        selected_port = int(port_number_entry.get())
    except ValueError:
        selected_port = 1024
    selected_game = "FH" if fh_btn["relief"] == "sunken" else "FM"
    initial_canvas.pack_forget()
    dashboard_canvas.pack(fill="both", expand=True)
    screen.attributes("-fullscreen", True)
    if start_callback:
        start_callback(selected_port, selected_game)

def select_choice(choice):
    if choice == 1:
        fh_btn.config(relief="sunken", bg="lightblue")
        fm_btn.config(relief="raised", bg="SystemButtonFace")
    else:
        fh_btn.config(relief="raised", bg="SystemButtonFace")
        fm_btn.config(relief="sunken", bg="lightblue")


ip = GetIPAddr
IPAddr = ip.getIp()
print(IPAddr)


screen = Tk()
screen.title("Forza Dashboard")
title_icon = ImageTk.PhotoImage(file="assets/speedometer.png")
screen.iconphoto(True, title_icon)

# Get actual screen size
screen_width = screen.winfo_screenwidth()
screen_height = screen.winfo_screenheight()

# Create a canvas that fills the screen
initial_canvas = Canvas(screen, width=screen_width, height=screen_height, bg="#ffffff", highlightthickness=0)
initial_canvas.pack(fill="both", expand=True)

# Center point
cx = screen_width // 2
cy = screen_height // 2
print(screen_width)
print(screen_height)

font_1_path = os.path.join("assets", "Camieis-YvBL.ttf")
ctypes.windll.gdi32.AddFontResourceW(font_1_path)
Camieis = tkFont.Font(family="Camieis", size=40)
Camieis_small = tkFont.Font(family="Camieis", size=20)

dashboard_canvas = Canvas(screen, width=screen_width, height=screen_height, bg="#3f3f3f", highlightthickness=0)


# welcome screen
title=Label(screen, font=("camieis", 60), text="Forza Dashboard", fg="black", bg="#ffffff")
initial_canvas.create_window(cx, cy-300, window=title)

instructions_text = (
    "Instructions:\n"
    '- Your IP adress is: "' + IPAddr + '". Type this number in FORZA under "Data Output IP"\n'
    '- Enter a port number below, make sure it is identical to what is entered in the game settings\n' 
    '- Select game(fh5 + fh4 / fm7)\n'
    '- Press start to begin recieving data\n'
    "- Press F11 to enter fullscreen, and Escape to exit it.\n"
)
instructions_label = Label(screen,text=instructions_text,font=("Segoe UI", 20), fg="white", bg="#3f3f3f", justify="left", wraplength=800)
initial_canvas.create_window(cx, cy-50, window=instructions_label)

port_number_label = Label(screen,text="Port Number: ",font=("Segoe UI", 20), fg="black", bg="#ffffff")
initial_canvas.create_window(cx-300, cy+170, window=port_number_label)
port_number_label_2 = Label(screen,text="(0 - 65536)",font=("Segoe UI", 16), fg="black", bg="#ffffff")
initial_canvas.create_window(cx-300, cy+200, window=port_number_label_2)
port_number_entry = Entry(screen, bg='white', borderwidth=1, relief='solid', font=Camieis_small, width=10)
initial_canvas.create_window(cx-160, cy+173, window=port_number_entry)

fh_btn = Button(screen, text="FH4/FH5", width=10, font=("Segoe UI", 17), command=lambda: select_choice(1))
initial_canvas.create_window(cx, cy+173, window=fh_btn)
fm_btn = Button(screen, text="FM7", width=10, font=("Segoe UI", 17), command=lambda: select_choice(2))
initial_canvas.create_window(cx+150, cy+173, window=fm_btn)
select_choice(1)


next_button = Button(screen, text="Start", font=("Camieis", 24), command=switch_to_dashboard)
initial_canvas.create_window(cx+305, cy+173, window=next_button)





# Gear
gear = Label(screen, font=("Impact", 250), text="N", fg="white", bg="#3f3f3f")
dashboard_canvas.create_window(cx, cy, window=gear)
gear_label = Label(screen, font=("Impact", 60), text="Gear", bg="#3f3f3f", fg="white")
dashboard_canvas.create_window(cx, cy + 160, window=gear_label)


# RPM
rpm = Label(screen, font=("Impact", 80), text="00000", fg="white", bg="#3f3f3f")
dashboard_canvas.create_window(cx, cy - 250, window=rpm)
rpm_label = Label(screen, font=("Impact", 20), text="RPM", fg="white", bg="#3f3f3f")
dashboard_canvas.create_window(cx, cy - 180, window=rpm_label)

# Speed
speed = Label(screen, font=("Impact", 100), text="000", fg="white", bg="#3f3f3f")
dashboard_canvas.create_window(cx, cy + 280, window=speed)
speed_label = Label(screen, font=("Impact", 30), text="km/h", fg="white", bg="#3f3f3f")
dashboard_canvas.create_window(cx, cy + 370, window=speed_label)

# Lap Number
lap = Label(screen, font=("Impact", 70), text="00", fg="black")
dashboard_canvas.create_window(cx-cx+220, cy-cy+110, window=lap, anchor="nw")
lap_label = Label(screen, font=("Impact", 30), text="Lap", fg="white", bg="#3f3f3f")
dashboard_canvas.create_window(cx-cx+16+220, cy-cy+236, window=lap_label, anchor="nw")

# Position
pos = Label(screen, font=("Impact", 70), text="00", fg="black")
dashboard_canvas.create_window(cx-cx+40, cy-cy+110, window=pos, anchor="nw")
pos_label = Label(screen, font=("Impact", 30), text="POS", fg="white", bg="#3f3f3f")
dashboard_canvas.create_window(cx-cx+16+40, cy-cy+236, window=pos_label, anchor="nw")

# Current Lap
current_lap = Label(screen, font=("Impact", 50), text="00:00:000", fg="white", bg="#3f3f3f")
dashboard_canvas.create_window(cx-cx+20, cy, window=current_lap, anchor="w")

# last Lap
last_lap = Label(screen, font=("Impact", 50), text="00:00:000", fg="#B6B63F", bg="#3f3f3f")
dashboard_canvas.create_window(cx-cx+20, cy+80, window=last_lap, anchor="w")

# best Lap
best_lap = Label(screen, font=("Impact", 50), text="00:00:000", fg="#008200", bg="#3f3f3f")
dashboard_canvas.create_window(cx-cx+20, cy+160, window=best_lap, anchor="w")

# throttle
thrtl = Label(screen, font=("Impact", 40), text="000", fg="white", bg="#3f3f3f")
dashboard_canvas.create_window(cx+300, cy-cy+200, window=thrtl)
thrtl_label = Label(screen, font=("Impact", 20), text="Thrtl", fg="#B6B63F", bg="#3f3f3f")
dashboard_canvas.create_window(cx+300, cy-cy+250, window=thrtl_label)

# brake
brake = Label(screen, font=("Impact", 40), text="000", fg="white", bg="#3f3f3f")
dashboard_canvas.create_window(cx+430, cy-cy+200, window=brake)
brake_label = Label(screen, font=("Impact", 20), text="Brake", fg="#B6B63F", bg="#3f3f3f")
dashboard_canvas.create_window(cx+430, cy-cy+250, window=brake_label)

# Fuel
fuel = Label(screen, font=("Impact", 30), text="000", fg="white", bg="#3f3f3f")
dashboard_canvas.create_window(cx+380, cy-30, window=fuel)
fuel_img_path = os.path.join("assets", "gas-station.png")
fuel_img = Image.open(fuel_img_path)
fuel_img_resized = fuel_img.resize((40, 40)) 
fuel_img = ImageTk.PhotoImage(fuel_img_resized)
fuel_icon = Label(screen, image=fuel_img, bg="#3f3f3f")
dashboard_canvas.create_window(cx+320, cy-30, window=fuel_icon)

# Tire Tempreture
tire_temp_FL = Label(screen, font=("Impact", 30), text="000", fg="black", bg="#FFFFFF")
dashboard_canvas.create_window(cx+350-50, cy+200-60, window=tire_temp_FL)
tire_temp_FR = Label(screen, font=("Impact", 30), text="000", fg="black", bg="#FFFFFF")
dashboard_canvas.create_window(cx+350+50, cy+200-60, window=tire_temp_FR)
tire_temp_RL = Label(screen, font=("Impact", 30), text="000", fg="black", bg="#FFFFFF")
dashboard_canvas.create_window(cx+350-50, cy+200+60, window=tire_temp_RL)
tire_temp_RR = Label(screen, font=("Impact", 30), text="000", fg="black", bg="#FFFFFF")
dashboard_canvas.create_window(cx+350+50, cy+200+60, window=tire_temp_RR)
tire_temp_img_path = os.path.join("assets", "weather.png")
tire_temp_img = Image.open(tire_temp_img_path)
tire_temp_img_resized = tire_temp_img.resize((60, 60)) 
tire_temp_img = ImageTk.PhotoImage(tire_temp_img_resized)
tire_temp_icon = Label(screen, image=tire_temp_img, bg="#3f3f3f")
dashboard_canvas.create_window(cx+350, cy+200, window=tire_temp_icon)


def exit_fullscreen(event):
    screen.attributes("-fullscreen", False)
    print("workssss")

def enter_fullscreen(event):
    screen.attributes("-fullscreen", True)
screen.bind("<Escape>", exit_fullscreen)
screen.bind("<F11>", enter_fullscreen)



def update_screen(SPEED, GEAR, RPM, POS, LAP_TIME, LAST_LAP_TIME, BEST_LAP_TIME, LAP_NUMBER, ACCEL, TTFL, TTFR, TTRL, TTRR, BRAKE, FUEL):
    def update_values():
        speed.config(text=int(SPEED))
        gear.config(text=GEAR)
        rpm.config(text= int(RPM))
        pos.config(text=POS)
        current_lap.config(text=LAP_TIME)
        last_lap.config(text=LAST_LAP_TIME)
        best_lap.config(text=BEST_LAP_TIME)
        lap.config(text=LAP_NUMBER)
        thrtl.config(text=ACCEL/2.55)
        tire_temp_FL.config(text=math.ceil(((TTFL-32)*5/9) * 10) / 10)
        tire_temp_FR.config(text=math.ceil(((TTFR-32)*5/9) * 10) / 10)
        tire_temp_RL.config(text=math.floor(((TTRL-32)*5/9) * 10) / 10)
        tire_temp_RR.config(text=math.floor(((TTRR-32)*5/9) * 10) / 10)
        brake.config(text=BRAKE/2.55)
        fuel.config(text=FUEL)
    screen.after(0, update_values)

def set_start_callback(callback):
    global start_callback
    start_callback = callback

def launch_gui():
    screen.mainloop()


