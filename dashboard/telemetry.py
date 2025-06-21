import socket
import threading

class TelemetryReceiver:
    def __init__(self, port=57312):
        self.host = "0.0.0.0"
        self.port = port
        self.running = False
        self.data_callback = None

    def start(self):
        self.running = True
        thread = threading.Thread(target=self._receive) # Creates a background thread to run the recieve method
        thread.daemon = True
        thread.start()

    def _receive(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((self.host, self.port))
        while self.running:
            data, _ = sock.recvfrom(1024) #Set buffer size ; The underscore is used to ignore the 2nd return of recvfrom()
            if self.data_callback:
                self.data_callback(data)
                
    
    def stop(self):
        self.running = False
