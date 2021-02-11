
"""
Tool to be used on the host to listen on the serial Pico port.
"""

import time
import serial
ser = serial.Serial('/dev/ttyACM0')
ser.flushInput()

print("This will keep listening to the device, stop with Ctrl-C")
print("Be aware to stop this when flashing stuff to the Pico.")
print("Start listening...")
while True:
    try:
        ser_bytes = ser.readline()
        decoded_bytes = ser_bytes[0:len(ser_bytes)-2].decode("utf-8")
        print(decoded_bytes)
    except Exception as e:
        print(e)
        break
    except KeyboardInterrupt:
        print("User wants to stop, stopping and closing port...")
        break

ser.close()
time.sleep(0.2)
print("The port is closed")
