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
        }
        print("Speed:", parsed["speed_kph"]*3.6, "Gear:", parsed["gear"], "rpm:", parsed["rpm"], "max_rpm", parsed["max_rpm"]) 
    except struct.error as e:
        print("Unpack error:", e)
    

receiver = TelemetryReceiver()
receiver.data_callback = handle_data
receiver.start()

print("test2")

# Keep the program running forever
import time
while True:
    time.sleep(1)



