#!/usr/bin/env python3

import simpleaudio as sa
import RPi.GPIO as GPIO


# Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



# Setup media
intro1 = "intro0101.wav"
intro2 = "intro0102.wav"
intro3 = "intro0103.wav"

workout1 = ["intro0101.wav","lyd0101.wav", "intro0102.wav", "lyd0102.wav", "intro0103.wav", "lyd0103.wav"]
workout2 = ["intro0201.wav","lyd0201.wav", "intro0202.wav", "lyd0202.wav", "intro0203.wav", "lyd0203.wav"]






def spillAvLyd(filnavn: str):
    wave_obj = sa.WaveObject.from_wave_file(filnavn)
    play_obj = wave_obj.play()
    play_obj.wait_done() # denne blokkerer..


def spillWorkout(lst):
    for m in lst:
        spillAvLyd(m)


#def button_callback(channel):
    #spillWorkout(workout1)

#GPIO.add_event_detect(10, GPIO.RISING, callback=button_callback)

#message = input("press Enter to quit\n")

#while True:
    #if GPIO.input(10) == GPIO.HIGH:
        #spillWorkout(workout1)
#spillWorkout(workout1)

GPIO.cleanup()