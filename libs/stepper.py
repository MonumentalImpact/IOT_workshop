from time import sleep_ms
from machine import Pin, Timer

# only tested for uln2003
class Stepper:
    
    """
    For controlling stepper motors using ULN2003 driver.
    
    pin1, pin2, pin3, pin4 : ESP32 pins connected to IN1-IN4 on the ULN2003 board can be either an integer or Pin object
    mode : 'HALF_STEP' (default) recommended by stepper motor datasheet (http://www.jangeox.be/2013/10/stepper-motor-28byj-48_25.html)
            'FULL_STEP' should give more torque
    delay : time between steps in milliseconds. changes speed of rotation. default set depends on mode
    """
    FULL_ROTATION = int(4075.7728395061727 / 8) 

    HALF_STEP = [
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 1],
    ]

    FULL_STEP = [
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 0, 1]
    ]
    def __init__(self, pin1, pin2, pin3, pin4, mode='HALF_STEP', delay=None):
    	if mode=='FULL_STEP':
        	self.mode = self.FULL_STEP
        else:
        	self.mode = self.HALF_STEP
        self.pin1 = pin1 if type(pin1) == Pin else Pin(pin1,Pin.OUT)
        self.pin2 = pin2 if type(pin2) == Pin else Pin(pin2,Pin.OUT)
        self.pin3 = pin3 if type(pin3) == Pin else Pin(pin3,Pin.OUT)
        self.pin4 = pin4 if type(pin4) == Pin else Pin(pin4,Pin.OUT)
        if delay == None:
            if mode == 'FULL_STEP':
                delay = 10
            else:
                delay = 1
        self.delay = delay  # Recommend 10+ for FULL_STEP, 1 is OK for HALF_STEP
        
        # Initialize all to 0
        self.reset()
        
    def step(self, count, delay=None):
        """Rotate count steps. a negative count means backwards"""
        direction = 1 if count > 0 else -1
        if delay == None:
            delay = self.delay
        for x in range(abs(count)):
            for bit in self.mode[::direction]:
                self.pin1(bit[0])
                self.pin2(bit[1])
                self.pin3(bit[2])
                self.pin4(bit[3])
                sleep_ms(delay)
        self.reset()
        
    def angle(self, r, delay=None):
    	self.step(int(self.FULL_ROTATION * r / 360), delay)
    	
    def reset(self):
        # Reset to 0, no holding, these are geared, you can't move them
        self.pin1(0) 
        self.pin2(0) 
        self.pin3(0) 
        self.pin4(0)
 