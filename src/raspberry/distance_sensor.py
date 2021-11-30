#!/usr/bin/python3

from gpiozero import DistanceSensor, LED, Button
from time import sleep
import signal
from os import system

redLED = LED(19)
yellowLED = LED(13)
greenLED = LED(6)
sensor = DistanceSensor(echo=17, trigger=27)
buzzer = LED(20)
button = Button(21)
mute = False


def toggle_mute():
    global mute
    mute = not mute


def distance(dist):
    if dist > 0.20:
        greenLED.on()
        yellowLED.off()
        redLED.off()
    elif dist > 0.05:
        yellowLED.on()
        greenLED.off()
        redLED.off()
    else:
        redLED.on()
        yellowLED.off()
        greenLED.off()


def sound(dist):
    if not mute:        
        buzzer.on()
        sleep(0.2)
        buzzer.off()
        sleep(dist*5) 


try:
    button.when_pressed = toggle_mute
    while True:
        dist = sensor.distance
        distance(dist)        
        sound(dist)
        print("Distance: ", dist*100)        
except KeyboardInterrupt:
    exit(0)
        


