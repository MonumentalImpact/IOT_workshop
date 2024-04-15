#test_stepper
#
# connect wires from ESP32 pins 26, 25, 33, 32 to the IN1, IN2, IN3, IN4 on the
# stepper controller board
# connect + and - from the stepper controller board to a power supply. If you're connecting more
#	than one motor, it's a good idea to use a power supply separate from the ESP32. They should all
#	connect to a common ground. The motors can pull a lot of current, which can cause the ESP32 to
#	lose power and fail.

from stepper import Stepper

s1 = Stepper( 26, 25, 33, 32, mode='HALF_STEP', delay=1)
s1.step(100)
s1.step(-100) 
s1.angle(180)
s1.angle(-360)
s1.angle(180)
