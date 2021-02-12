
import machine
import utime

led = machine.Pin(3, machine.Pin.OUT)

def main():
    while True:
        print("blink, print")
        led.value(1)
        utime.sleep(1)
        led.value(0)
        utime.sleep(1)
