from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime
 

WIDTH  = 128                                            # oled display width
HEIGHT = 64                                             # oled display height

button_sw0 = Pin(9,Pin.IN,Pin.PULL_UP)
button_sw2 = Pin(7,Pin.IN,Pin.PULL_UP)

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=200000)       # Init I2C using pins GP8 & GP9 (default I2C0 pins)
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config
 
 
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display
 

x=10
y=50
ui_list = []

while True:
    oled.fill(0)
    user_in = input() #ask input
    ui_list.append(user_in) # append to list
    utime.sleep(0.05) #sleep 50ms
    for i in range(len(ui_list)): # go through the list
        oled.text(ui_list[(len(ui_list)-(i+1))],x,(y-(i*10))) # print last in list to bottom and previous 10px above it 
    oled.show()#after for loop show list
        

        