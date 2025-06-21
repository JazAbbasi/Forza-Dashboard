import socket
import struct

# Configure based on Forza settings
FORZA_IP = '192.168.1.34'  # Or your machine's IP
FORZA_PORT = 5555    # Or the port you set in Forza

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((FORZA_IP, FORZA_PORT))

print(f"Listening for Forza telemetry on {FORZA_IP}:{FORZA_PORT}")

try:
    while True:
        data, addr = sock.recvfrom(1024)  # Adjust buffer size if needed
        print(f"Received telemetry: {addr}")

        # Example: Unpack a few known fields (this will vary based on Forza version)
        # This is a placeholder; you need to match the actual Forza telemetry format.
        # For instance, 'f' for float, 'i' for integer.
        try:
            # Example format for a hypothetical Forza V2 telemetry (adjust as needed)
            # This is a simplified example; actual Forza telemetry is more complex.
            
            # Access extracted data:
            # game_state = telemetry_data[0]
            # speed = telemetry_data[1]
            # rpm = telemetry_data[2]
            # gear = telemetry_data[3]
            # steering_angle = telemetry_data[4]

            # Print or process the data
            print(f"Received telemetry: {addr}")

        except struct.error as e:
            print(f"Error unpacking data: {e}")
            print(f"Raw data: {data}")

except KeyboardInterrupt:
    print("Stopping telemetry receiver.")
finally:
    sock.close()