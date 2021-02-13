# MicroPython TM1637 quad 7-segment LED display driver examples

# RsPI Pico
# D2 (GP6) ------- DIO
# D3 (GP7) ------- CLK
# 3V3 ------------ VCC
# G -------------- GND

import tm1637
from machine import Pin
tm = tm1637.TM1637(clk=Pin(7), dio=Pin(6))


def main():
    # all LEDS on "88:88"
    tm.write([127, 255, 127, 127])
    tm.write(bytearray([127, 255, 127, 127]))
    tm.write(b'\x7F\xFF\x7F\x7F')
    tm.show('8888', True)
    tm.numbers(88, 88, True)
