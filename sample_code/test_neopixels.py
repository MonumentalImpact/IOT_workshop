from machine import Pin
from neopixel import NeoPixel
from time import sleep

npixels = 30
np = NeoPixel(Pin(27, Pin.OUT), npixels)   # create NeoPixel driver on GPIO0 for 8 pixels

np[0] = (0, 255, 255) # set the first pixel to white
np.write()              # write data to all pixels

for n in range(256):
    np.fill( (255-n,255-n,255-n))
    np.write()
    sleep(0.01)
    
for _ in range(5):
    for n in range(npixels):
        np.fill((0,0,0))
        np[n] = (255,0,0)
        np.write()
        sleep(0.01)
        
np.fill((0,0,0))
np.write()