
import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)

def main():
    while True:
        print("blink, print")
        led_onboard.value(1)
        utime.sleep(1)
        led_onboard.value(0)
        utime.sleep(1)
