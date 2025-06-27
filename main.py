from dashboard.telemetry import TelemetryReceiver
from dashboard.gui import update_screen, launch_gui
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
            "speed_kph": struct.unpack_from('<f', data, 256)[0],
            "gear": struct.unpack_from('<b', data, 319)[0],
            "rpm":struct.unpack_from('<f', data, 16)[0],
            "max_rpm":struct.unpack_from('<f', data, 8)[0],
            "fuel":struct.unpack_from('<f', data, 288)[0],
            "accel":struct.unpack_from('<B', data, 315)[0],
            "pos":struct.unpack_from('<B', data, 314)[0],
            "lap_time":struct.unpack_from('<f', data, 304)[0],
            "last_lap_time":struct.unpack_from('<f', data, 300)[0],
            "best_lap_time":struct.unpack_from('<f', data, 296)[0],
            "lap_number":struct.unpack_from('<H', data, 312)[0],
            "tire_temp_front_left":struct.unpack_from('<f', data, 268)[0],
            "tire_temp_front_right":struct.unpack_from('<f', data, 272)[0],
            "tire_temp_rear_left":struct.unpack_from('<f', data, 276)[0],
            "tire_temp_rear_right":struct.unpack_from('<f', data, 280)[0],
            

        }
        print("yo")
        print("Speed:", parsed["speed_kph"]*3.6, "Gear:",
               parsed["gear"], "rpm:", parsed["rpm"], "max_rpm", parsed["max_rpm"], "fuel:", parsed["fuel"], "accel:", parsed["accel"], "pos:", parsed["pos"], "lap:", format_time(parsed["lap_time"]), "RL:", parsed["tire_temp_rear_left"], "RR:", parsed["tire_temp_rear_right"])
        update_screen(parsed["speed_kph"]*3.6, parsed["gear"], parsed["rpm"], parsed["pos"], format_time(parsed["lap_time"]), format_time(parsed["last_lap_time"]), format_time(parsed["best_lap_time"]), parsed["lap_number"], parsed["accel"], parsed["tire_temp_front_left"], parsed["tire_temp_front_right"], parsed["tire_temp_rear_left"], parsed["tire_temp_rear_right"])
    except struct.error as e:
        print("Unpack error:", e)
    

receiver = TelemetryReceiver()
receiver.data_callback = handle_data
receiver.start()

print("test2")



launch_gui()


