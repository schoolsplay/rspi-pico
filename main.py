
import machine
import utime

led_green = machine.Pin(2, machine.Pin.OUT)
led_red  = machine.Pin(2, machine.Pin.OUT)

def reset_led():
    machine.Pin(2, machine.Pin.OUT).value(0)
    machine.Pin(3, machine.Pin.OUT).value(0)

def set_led(color="green"):
    print("set_led called with: {}".format(color))
    reset_led()
    if color == "green":
        led = machine.Pin(2, machine.Pin.OUT)
    else:
        led = machine.Pin(3, machine.Pin.OUT)
    led.value(1)


while True:
    set_led('red')
    utime.sleep(2)
    set_led('green')
    utime.sleep(2)
