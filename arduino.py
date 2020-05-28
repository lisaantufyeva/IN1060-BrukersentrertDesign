import serial
import RPi.GPIO as GPIO
import time
import pygame


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

NEXT = pygame.USEREVENT+1
currentplaylist = []
currenttrack = 0

def main():

    pygame.init()
    pygame.mixer.init(frequency = 48000)

    while True:
        print("loop")
        read_ser = ser.readline()
        handlePygameEvents()

        message = read_ser.decode("ASCII")
        if message != "":
            parts = message.strip().split(" ")
            message = ""
            print(parts)

            commando = parts[0]
            workout = parts[1]
            level = parts[2]

            commandfraArduino(commando, workout, level)

            #playWorkout(commando, workout, level)

def commandfraArduino(commando, workout, level):
    if (commando == "PLAY"):
        playWorkout(commando, workout, level)
    if (commando == "PAUSE"):
        pauseWorkout()


def playWorkout(commando, workout, level):
    global currentplaylist
    global currenttrack
    if (commando == "PLAY"):
        if (workout == "1"):
            if (level == "1"):
                currentplaylist = workout1nivaa1
            if (level == "2"):
                currentplaylist = workout1nivaa2
            if (level == "3"):
                currentplaylist = workout1nivaa3
            currenttrack = 0
        if (workout == "2"):
            if (level == "1"):
                currentplaylist = workout1nivaa1
            if (level == "2"):
                currentplaylist = workout1nivaa2
            if (level == "3"):
                currentplaylist = workout1nivaa3
            currenttrack = 0
            spillWorkout()

def spillWorkout():
    if len(currentplaylist) > 0 and  currenttrack < len(currentplaylist):
        pygame.mixer.music.load(currentplaylist[currenttrack])
        pygame.mixer.music.play()
        if playlistNotEmpty():
            pygame.mixer.music.set_endevent(NEXT)


def playlistNotEmpty():
    return currenttrack < len(currentplaylist)-1

def handlePygameEvents():
    global currenttrack
    for event in pygame.event.get():
        if event.type == NEXT:
            print("Pygame event: NEXT")
            currenttrack = (currenttrack + 1)
            spillWorkout()


def pauseWorkout():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()

def stopLyd():
    return


main()
GPIO.cleanup()