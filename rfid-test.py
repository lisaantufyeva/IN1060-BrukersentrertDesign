
#!/usr/bin/env python3

import simpleaudio as sa
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

# Setup GPIO
print("Setup GPIO")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Setup reader
print("Setup SimpleMFRC522")
reader = SimpleMFRC522()

# Setup media
intro1 = "media/intro0101.wav"
intro2 = "media/intro0102.wav"
intro3 = "media/intro0103.wav"

# Spilleliste Workout1
workout1nivaa1 = ["media/intro0101.wav","media/lyd0101.wav", "media/intro0102.wav", "media/lyd0102.wav", "media/intro0103.wav", "media/lyd0103.wav"]
workout1nivaa2 = ["media/intro0202.wav","media/lyd0202.wav"]
workout1nivaa3 = ["media/lyd0102.wav", "media/intro0103.wav", "media/lyd0103.wav"]


# Spilleliste Workout2
workout2nivaa1 = ["media/intro0101.wav","media/lyd0101.wav", "media/intro0102.wav", "media/lyd0102.wav", "media/intro0103.wav", "media/lyd0103.wav"]
workout2nivaa2 = ["media/intro0202.wav","media/lyd0202.wav"]
workout2nivaa3 = ["media/lyd0102.wav", "media/intro0103.wav", "media/lyd0103.wav"]

#Setup ID
workout1Id = "440026144656"
workout2Id = "726646219672"

# Main
def main():
    print("Start program")

    id = str(readFromReader())
    print("Lest id: " + id)

    sjekkId(id)
    GPIO.cleanup()



def spillAvLyd(filnavn: str):
    wave_obj = sa.WaveObject.from_wave_file(filnavn)
    play_obj = wave_obj.play()
    play_obj.wait_done() # denne blokkerer..


def stopLyd():
    play_obj.stop()

def spillWorkout(lst):
    for m in lst:
        spillAvLyd(m)


def button_callback(channel):
    spillWorkout(workout1)


def readFromReader():
    r = None
    try:
        print("prøv les")
        id, text = reader.read()
        print(id)
        print(text)
        r = id
    finally:
        #GPIO.cleanup()
        return r


def sjekkIdandPlay(id):
    if id == workout1Id:
        while True:
            if GPIO.input(10) == GPIO.HIGH:
                spillWorkout(workout1)


    if id == workout2Id:
        while True:
            if GPIO.input(10) == GPIO.HIGH:
                spillWorkout(workout2)
                if not play_obj.is_playing:
                    print("done")

def sjekkId(id):
    if id == workout1Id:
        while True:

            if GPIO.input(10) == GPIO.HIGH:
                print("Workout 1 nivå1")
                spillWorkout(workout1nivaa1)

            if GPIO.input(12) == GPIO.HIGH:
                print("Workout 1 nivå2")
                spillWorkout(workout1nivaa2)

            if GPIO.input(11) == GPIO.HIGH:
                print("Workout 1 nivå3")
                spillWorkout(workout1nivaa3)

    if id == workout2Id:
            while True:

                if GPIO.input(10) == GPIO.HIGH:
                    print("Workout 2 nivå1")
                    spillWorkout(workout2nivaa1)

                if GPIO.input(12) == GPIO.HIGH:
                    print("Workout 2 nivå2")
                    spillWorkout(workout2nivaa2)

                if GPIO.input(11) == GPIO.HIGH:
                    print("Workout 2 nivå3")
                    spillWorkout(workout2nivaa3)




#def button_callback(channel):
    #stopLyd()

#GPIO.add_event_detect(10, GPIO.RISING, callback=button_callback)


#message = input("press Enter to quit\n")




#while True:
    #if GPIO.input(10) == GPIO.HIGH:
        #spillWorkout(workout1)


#spillWorkout(workout1)

main()