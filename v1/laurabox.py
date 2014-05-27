"""
title: laura box
author: matt venn, 2014
license: GPL attribution share alike
"""
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#pin defs
buttons = [16,18]
in_jacks = [12,10]
out_jacks = [8,15]
leds = [13,11,7,5,3]
status_led = 3

for pin in buttons + in_jacks:
    #pull up
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
for pin in leds:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)
for pin in out_jacks:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

def button_int(channel):  
    time.sleep(0.1)
    state = GPIO.input(channel)
    print("%d button pressed on %d" % (state,channel))
    for inp,outp in zip(buttons + in_jacks,leds[0:4]):
        if channel == inp:
            GPIO.output(outp,not state)


for pin in buttons + in_jacks:
    GPIO.add_event_detect(pin, GPIO.BOTH, callback=button_int, bouncetime=30)

while True:
    time.sleep(1)
    GPIO.output(status_led,True)
    time.sleep(1)
    GPIO.output(status_led,False)
