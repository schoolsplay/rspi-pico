# MicroPython BME280 Humidity/temp/pressure driver examples

# RsPI Pico
# SCL (GP15) ------- SCL
# SDA (GP14) ------- SDA
# 3V3 -------------- VCC
# GND -------------- GND

import utime
from bme280 import BME280
from machine import I2C

i2c = I2C("X")
bme = BME280(i2c=i2c)

# Let the device come alive (read on forum that I2C sometimes need time)
utime.sleep_us(500)

def main():
    print(bme.temperature(), bme.pressure(), bme.humidity())
