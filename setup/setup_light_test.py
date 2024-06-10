from machine import Pin
from time import sleep

p = Pin(2, Pin.OUT)

print("Now flashing the on-board LED...")

for i in range(10):
    p.on()
    sleep(1)
    p.off()
    sleep(1)
    
print("All done!")
