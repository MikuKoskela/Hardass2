from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime
 
sensor_temp = machine.ADC(28)
conversion_factor = 3.3 / (65535)
 
WIDTH  = 128                                            # oled display width
HEIGHT = 64                                             # oled display height

button_sw0 = Pin(9,Pin.IN,Pin.PULL_UP)
button_sw2 = Pin(7,Pin.IN,Pin.PULL_UP)

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=200000)       # Init I2C using pins GP8 & GP9 (default I2C0 pins)
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config
 
 
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display
#starting location 
x=50
y=54
ufo = ("<=>")
while True: 
    oled.fill(0) #clear screen when starting
    oled.text(ufo, x, y)
    oled.show()
    utime.sleep(0.05)
    while button_sw0() == 0: #if sw0 pressed
        utime.sleep(0.1)
        x+=5
        if x >= 100:#limit ufo movement to stay in screen
            x=100
        oled.text(ufo, x, y)
    while button_sw2() == 0: #if sw2 pressed
        utime.sleep(0.1)
        x-=5
        if x <= 0:#limit ufo movement to stay in screen
            x=0
        oled.text(ufo, x, y)
        