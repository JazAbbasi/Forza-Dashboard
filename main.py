from dashboard.telemetry import TelemetryReceiver
from dashboard.gui import update_screen, launch_gui, set_start_callback
import struct
print("test")


def format_time(seconds_float):
    minutes = int(seconds_float) // 60
    seconds = int(seconds_float) % 60
    milliseconds = int((seconds_float - int(seconds_float)) * 1000)

    return f"{minutes:02}:{seconds:02}:{milliseconds:03}"

# When new data is received, this function will run
def handle_data(data):
    try:
        parsed = {
            "speed_kph": struct.unpack_from('<f', data, 244+position_value)[0],
            "gear": struct.unpack_from('<b', data, 307+position_value)[0],
            "rpm":struct.unpack_from('<f', data, 16)[0],
            "max_rpm":struct.unpack_from('<f', data, 8)[0],
            "fuel":struct.unpack_from('<f', data, 276+position_value)[0],
            "accel":struct.unpack_from('<B', data, 303+position_value)[0],
            "pos":struct.unpack_from('<B', data, 302+position_value)[0],
            "lap_time":struct.unpack_from('<f', data, 292+position_value)[0],
            "last_lap_time":struct.unpack_from('<f', data, 288+position_value)[0],
            "best_lap_time":struct.unpack_from('<f', data, 284+position_value)[0],
            "lap_number":struct.unpack_from('<H', data, 300+position_value)[0],
            "tire_temp_front_left":struct.unpack_from('<f', data, 256+position_value)[0],
            "tire_temp_front_right":struct.unpack_from('<f', data, 260+position_value)[0],
            "tire_temp_rear_left":struct.unpack_from('<f', data, 264+position_value)[0],
            "tire_temp_rear_right":struct.unpack_from('<f', data, 268+position_value)[0],
            "brake":struct.unpack_from('<B', data, 304+position_value)[0],
            

        }
        print("yo")
        print("Speed:", parsed["speed_kph"]*3.6, "Gear:",
               parsed["gear"], "rpm:", parsed["rpm"], "max_rpm", parsed["max_rpm"], "fuel:", parsed["fuel"], "accel:", parsed["accel"], "pos:", parsed["pos"], "lap:", format_time(parsed["lap_time"]), "RL:", parsed["tire_temp_rear_left"], "RR:", parsed["tire_temp_rear_right"])
        update_screen(parsed["speed_kph"]*3.6, parsed["gear"], parsed["rpm"], parsed["pos"], format_time(parsed["lap_time"]), format_time(parsed["last_lap_time"]), format_time(parsed["best_lap_time"]), parsed["lap_number"], parsed["accel"], parsed["tire_temp_front_left"], parsed["tire_temp_front_right"], parsed["tire_temp_rear_left"], parsed["tire_temp_rear_right"], parsed["brake"], parsed["fuel"])
    except struct.error as e:
        print("Unpack error:", e)

receiver = None
def on_start(port, game_mode):
    global position_value
    if game_mode == "FH": 
        position_value = 12 
    else: 
        position_value = 0
    print (position_value)

    global receiver
    receiver = TelemetryReceiver(port=port)
    receiver.data_callback = handle_data
    receiver.start()
    


print("test2")


set_start_callback(on_start)
launch_gui()


