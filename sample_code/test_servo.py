# https://github.com/pvanallen/esp32-getstarted/blob/master/docs/servo.md
from time import sleep
from servo import Servo

servos = []

#for MS18 servo, orange=signal(attach to control pin, this example uses 23), red=+5v, green=GND
max_angle = 180
servos.append( Servo( pin=23, freq=50, min_us=500, max_us=2500, angle=max_angle) )

#for MS24-F servo, white=signal, red=+5v(4.8-6.8V;2.1-2.7A), black=GND
# max_angle = 270
# servos.append( Servo( pin=22, freq=50, min_us=500, max_us=2500, angle=max_angle) )

def test_servo(s):
    #rotate through full range in 5 seconds
    for a in range(max_angle):
        s.write_angle(degrees=a)
        sleep(5.0/max_angle)
        
    sleep(3)
    s.write_angle(0)

for s in servos:
    test_servo(s)
