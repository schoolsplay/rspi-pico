
import utime
from machine import UART

uart_id = 0
brate = 115200

uart = UART(1, brate)
#uart.init(brate, bits=8, parity=None, stop=1)

txt = "Hello uart world\n"
arr = bytearray(txt, 'utf-8')

def main():
    while True:
        print("sending", txt)
        uart.write(arr)
        utime.sleep(1)



