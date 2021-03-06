"""
Starter for your script.
Be aware that this uses the buildin LED at pin 25 and a red LED at pin 2:
    constant green -> module is imported correctly
    constant red at pin 2 -> import or calling module.main failed

It will import the module in a try/except clause and then call the module 'main'
method also in a try/except clause.
If the onboard led is green everything is ok, otherwise the red led will be on
"""

import os
import machine

logfile = "main.log"
try:
    os.remove(logfile)
except:
    pass

def write_log(txt):
    """Use only in development!
    It can quickly fill your memory."""
    with open(logfile, 'a') as f:
        f.write(txt + '\n')

def reset_led():
    machine.Pin(25, machine.Pin.OUT).value(0)
    machine.Pin(2, machine.Pin.OUT).value(0)

def set_led(ok):
    #write_log("set_led called with: {}".format(state))
    reset_led()

    if ok:
        machine.Pin(25, machine.Pin.OUT).value(1)
    else:
        machine.Pin(2, machine.Pin.OUT).value(1)

reset_led()

try:
    #import test_tm as module
    #import test as module
    #import test_uart as module
    import test_bme as module
except Exception as e:
    print("Exception in main importing script")
    print(e)
    set_led(False)
else:
    print("Import script successful")
    set_led(True)
    try:
        module.main()
    except Exception as e:
        print("Exception in module.main")
        print(e)
        set_led(False)

machine.Pin(25, machine.Pin.OUT).value(0)

print("End of main")



