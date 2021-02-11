import os
import machine

logfile = "main.log"
try:
    os.remove(logfile)
except:
    pass

led_green = machine.Pin(2, machine.Pin.OUT)
led_red  = machine.Pin(2, machine.Pin.OUT)

def write_log(txt):
    """Use only in development!
    It can quickly fill your memory."""
    with open(logfile, 'a') as f:
        f.write(txt + '\n')

def reset_led():
    machine.Pin(2, machine.Pin.OUT).value(0)
    machine.Pin(3, machine.Pin.OUT).value(0)

def set_led(color="green"):
    write_log("set_led called with: {}".format(color))
    reset_led()
    if color == "green":
        led = machine.Pin(2, machine.Pin.OUT)
    else:
        led = machine.Pin(3, machine.Pin.OUT)
    led.value(1)

reset_led()

try:
    import test as module
    #import test_uart as module
except (Exception, KeyboardInterrupt) as e:
    print("Exception in main importing script")
    print(e)
    set_led('red')
else:
    print("Import script successful")
    set_led()
    module.main()

print("End of main")



