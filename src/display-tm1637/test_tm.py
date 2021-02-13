# MicroPython TM1637 quad 7-segment LED display driver examples

# RsPI Pico
# D2 (GP6) ------- DIO
# D3 (GP7) ------- CLK
# 3V3 ------------ VCC
# G -------------- GND
import utime

import tm1637
from machine import Pin
tm = tm1637.TM1637(clk=Pin(5), dio=Pin(4))
tm.write([0, 0, 0, 0])

def main():
    i = 0
    while i <= 100:
        txt = '%04d' % i
        tm.show(txt, True)
        i += 1
        utime.sleep_us(1000)
