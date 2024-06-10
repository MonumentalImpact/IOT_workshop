from machine import Pin, PWM

pwm0 = PWM(Pin(22), freq=5000, duty_u16=32768) # create PWM object from a pin
freq = pwm0.freq()         # get current frequency
pwm0.freq(1000)            # set PWM frequency from 1Hz to 40MHz

duty = pwm0.duty()         # get current duty cycle, range 0-1023 (default 512, 50%)
pwm0.duty(256)             # set duty cycle from 0 to 1023 as a ratio duty/1023, (now 25%)
