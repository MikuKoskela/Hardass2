from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime
 

WIDTH  = 128                                            # oled display width
HEIGHT = 64                                             # oled display height

button_sw0 = Pin(9,Pin.IN,Pin.PULL_UP)
button_sw1 = Pin(8,Pin.IN,Pin.PULL_UP)
button_sw2 = Pin(7,Pin.IN,Pin.PULL_UP)

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=200000)       # Init I2C using pins GP8 & GP9 (default I2C0 pins)
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config
 
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display
 
x=0
y=32

while True:
    oled.text(".",x,y)
    utime.sleep(0.025) #sleep 200ms
    oled.show()
    x+=1
    if button_sw0() == 0: #if sw0 pressed move down
        y+=1
    
    if button_sw1() == 0: #if sw1 pressed start over
        oled.fill(0) #clear screen
        x=0
        y=32
        
    if button_sw2() == 0: #if sw2 pressed move up
        y-=1
        
    
    if x==124: # when close to end start from left
        x=0