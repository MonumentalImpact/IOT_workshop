from stepper import Stepper

s1 = Stepper( 26, 25, 33, 32, mode='HALF_STEP', delay=1)
s1.step(100)
s1.step(-100) 
s1.angle(180)
s1.angle(-360) 