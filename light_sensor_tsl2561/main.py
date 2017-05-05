import time
from machine import I2C
import tsl2561

# SDA='P23', SCL='P22'
i2c = I2C(0, I2C.MASTER, baudrate=100000, pins=('P23', 'P22'))
addr = i2c.scan()
print("Device addresses: ", addr)
addr = addr[0]

tsl = tsl2561.TSL2561(i2c, addr)

while True:
    lum = tsl.read()
    print("Lum: ", lum)
    time.sleep(1)
