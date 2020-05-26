import serial
import RPi.GPIO as GPIO
import time
import simpleaudio as sa

#Spilleliste Workout 1
workout1nivaa1 = ["media/intro0101.wav","media/lyd0101.wav"]
workout1nivaa2 = ["media/intro0202.wav","media/lyd0202.wav"]
workout1nivaa3 = ["media/intro0103.wav","media/lyd0103.wav"]


# Spilleliste Workout 2
workout2nivaa1 = ["media/intro0101.wav","media/lyd0101.wav"]
workout2nivaa2 = ["media/lyd0102.wav"]
workout2nivaa3 = ["media/lyd0102.wav"]


ser = serial.Serial("/dev/ttyACM0", 9600)
ser.baudrate = 9600
#def blink(pin):

    #GPIO.output(pin, GPIO.HIGH)
    #time.sleep(1)
    #GPIO.output(pin, GPIO.LOW)
    #time.sleep(1)
    #return

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(11,GPIO.OUT)
def main():

    while True:
        read_ser = ser.readline()
        message = read_ser.decode("ASCII")
        parts = message.strip().split(" ")
        print(parts)

        commando = parts[0]
        workout = parts[1]
        level = parts[2]

        print(commando)
        print(workout)

        print(level)
        playWorkout(commando, workout, level)

def playWorkout(commando, workout, level):

    if (commando == "Play"):
        if (workout == "1"):
            if (level == "1"):
                spillWorkout(workout1nivaa1)
    if (commando == "Play"):
        if (workout == "1"):
            if (level == "2"):
                spillWorkout(workout1nivaa2)
    if (commando == "Play"):
        if (workout == "1"):
            if (level == "3"):
                spillWorkout(workout1nivaa2)



def spillAvLyd(filnavn: str):
    wave_obj = sa.WaveObject.from_wave_file(filnavn)
    play_obj = wave_obj.play()
    play_obj.wait_done() # denne blokkerer..


def stopLyd():
    play_obj.stop()

def spillWorkout(lst):
    for m in lst:
        spillAvLyd(m)

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

main()
GPIO.cleanup()