from pyb import UART
from machine import Pin
uart = UART(2,9600)

while True:
    if uart.any():
        a = uart.read()
        print(a)
        if a == b'forward':
            tm = pyb.Timer(4, freq =1000)
            pwm = tm.channel(1 , mode = pyb.Timer.PWM, pin = pyb.Pin('PD14'))
            pwm.pulse_width_percent(80)
            
            tm = pyb.Timer(4, freq =1000)
            pwm = tm.channel(2 , mode = pyb.Timer.PWM, pin = pyb.Pin('PD15'))
            pwm.pulse_width_percent(80)
            
            pyb.delay(50)
            
            p14 = Pin(Pin('PD14'), Pin.OUT)
            p15 = Pin(Pin('PD15'), Pin.OUT)
            p14.off()
            p15.off()
            
            

            continue

           
        if a == b'left':

            
            tm = pyb.Timer(4, freq =1000)
            pwm = tm.channel(2 , mode = pyb.Timer.PWM, pin = pyb.Pin('PD15'))
            pwm.pulse_width_percent(80)
            
            pyb.delay(50)
            
            p14 = Pin(Pin('PD14'), Pin.OUT)
            p15 = Pin(Pin('PD15'), Pin.OUT)
            p14.off()
            p15.off()
            
            

            
            continue
 
 
 
 
            
        if a == b'right':
            tm = pyb.Timer(4, freq =1000)
            pwm = tm.channel(1 , mode = pyb.Timer.PWM, pin = pyb.Pin('PD14'))
            pwm.pulse_width_percent(80)
             
            
            pyb.delay(50)
            
            p14 = Pin(Pin('PD14'), Pin.OUT)
            p15 = Pin(Pin('PD15'), Pin.OUT)
            p14.off()
            p15.off()
            
            
            

            continue


           