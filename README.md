#Setup and develop on Linux

###See also the Pico Ebook

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

To develop on linux for pico you need the micropython package.
The snap is at this moment the same version as the image for pico

> sudo snap install micropython

###Setup Pycharm for MicroPython

Taken from: https://blog.jetbrains.com/pycharm/2018/01/micropython-plugin-for-pycharm/

1. Install MicroPython Plugin for PyCharm. After installing PyCharm and opening, 
   go to File>Settings>Plugins>Marketplace and search for MicroPython. Install it.
2. enable MicroPython support for your project in 
   File>Settings>Languages & Frameworks>MicroPython and specify your device there: ESP8266
3. Setup a py3.6 virtual environment and set it as the pycharm interpreter

> python3.6 -m venv .venv

## Run script from pycharm on the Pico
As pycharm doesn't have (yet?) support for the Pico you can use the simple ide Thonny
as the way to run a script developed in pycharm on the Pico by using Thonny as an interpreter :-)
Install latest version of thonny by pip (on my system I had to install tkinter systemwide)
    
>pip3 install thonny
> 
>sudo apt-get install python3.6-tkinter
> 
> thonny

Edit Thonny to have the correct interpreter "Pico"

Edit the run/debug configuration > Template > Bash/shell
Set as shell interpreter: /home/stas/Github/SchoolsplayRepos/Pico/.venv/bin/thonny

Now thonny will start with the script loaded and connected to Pico.
Hit the "run" button to run the script on Pico








