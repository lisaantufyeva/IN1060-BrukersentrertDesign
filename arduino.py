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


ser = serial.Serial("/dev/ttyACM1", 115200, timeout=1)
ser.baudrate = 115200

def main():

    while True:
        read_ser = ser.readline()

        message = read_ser.decode("ASCII")
        if message != "":
            parts = message.strip().split(" ")
            message = ""
            print(parts)

            commando = parts[0]
            workout = parts[1]
            level = parts[2]

            playWorkout(commando, workout, level)

def commandfraArduino(commando, workout, level):
    if (commando == "PLAY"):
        playWorkout(commando, workout, level);


def playWorkout(commando, workout, level):
    if (commando == "PLAY"):
        if (workout == "1"):
            if (level == "1"):
                spillWorkout(workout1nivaa1)
            if (level == "2"):
                spillWorkout(workout1nivaa2)
            if (level == "3"):
                spillWorkout(workout1nivaa2)

def spillWorkout(lst):
    for m in lst:
        spillAvLyd(m)

def spillAvLyd(filnavn: str):
    wave_obj = sa.WaveObject.from_wave_file(filnavn)
    play_obj = wave_obj.play()
    #play_obj.wait_done() # denne blokkerer..


def stopLyd():
    play_obj.stop()


main()
GPIO.cleanup()