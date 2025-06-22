from dashboard.telemetry import TelemetryReceiver
import struct
print("test")

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
            "lap":struct.unpack_from('<f', data, 304)[0],
        }
        print("Speed:", parsed["speed_kph"]*3.6, "Gear:",
               parsed["gear"], "rpm:", parsed["rpm"], "max_rpm", parsed["max_rpm"], "fuel:", parsed["fuel"], "accel:", parsed["accel"], "pos:", parsed["pos"], "lap:", format_time(parsed["lap"])) 
    except struct.error as e:
        print("Unpack error:", e)
    

receiver = TelemetryReceiver()
receiver.data_callback = handle_data
receiver.start()

print("test2")
def format_time(seconds_float):
    minutes = int(seconds_float) // 60
    seconds = int(seconds_float) % 60
    milliseconds = int((seconds_float - int(seconds_float)) * 1000)

    return f"{minutes:02}:{seconds:02}:{milliseconds:03}"

# Keep the program running forever
import time
while True:
    time.sleep(1)



