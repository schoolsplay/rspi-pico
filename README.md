# Setup and develop on Linux

### See also the Pico Ebook

To "flash" the micropython image to the pico:
https://www.raspberrypi.org/documentation/pico/getting-started/

To connect from your Linux host by USB use the minicon package to connect 
to the serial port

>sudo apt install minicom
> 
>sudo minicom -o -D /dev/ttyACM0

Hit a few time the enter key to get the prompt.
Use Ctrl-D to reboot the MicroPython to get an information text
for the MicroPython version

### Setup Pycharm for MicroPython

Taken from: https://blog.jetbrains.com/pycharm/2018/01/micropython-plugin-for-pycharm/

1. Install MicroPython Plugin for PyCharm. After installing PyCharm and opening, 
   go to File>Settings>Plugins>Marketplace and search for MicroPython. Install it.
2. enable MicroPython support for your project in 
   File>Settings>Languages & Frameworks>MicroPython and specify your device there: pyboard
3. Set as device path: /dev/ttyACM0
4. Setup a py3.6 virtual environment and set it as the pycharm interpreter

> python3.6 -m venv .venv
> 
> source ./venv/bin/activate
> 
> python3 -m pip install -r requirements.txt

## Run script from pycharm on the Pico

Create a script with the name main.py.
Use "main.py" as that is the file name that get run automatically by pico when it starts/reboots

As pycharm doesn't have (yet?) support for the Pico you can use the "pyboard" device 
in the micropython plugin flash the code to the pico.
Setup Run>Edit configuration>Micropython
Hit the "+" to add a configuration > Flash main.py

Right click on main.py and choose 'Run Flash main.py' to put your main.py onto the pico.

## Connect to Pico stdout/stderr from the pycharm
Run a script that prints something (or use this for debugging to show a traceback)
While it runs go to Tools>MicroPython>Micropython REPL, do a ctrl+d to quit the current
shell and it will show the stdout/stderr streams.
Don't forget to shut it down again by clicking on the little x in the "local" tab
otherwise you will get an error when you try to flash again: "could not enter raw repl"








