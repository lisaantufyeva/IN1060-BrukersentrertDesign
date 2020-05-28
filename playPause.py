import pygame



NEXT = pygame.USEREVENT+1


currenttrack = 0

workout1nivaa1 = ["/share/skolearbeid/media/intro0101.mp3","/share/skolearbeid/media/lyd0101.mp3"]

#paused = False




def main():

    playWorkout(workout1nivaa1, currenttrack)


def playWorkout(lst, currenttrack):

#initialize mixer to play music
    pygame.init()
    pygame.mixer.init(frequency = 48000)



    antall_filer = len(lst)

#play first track
    pygame.mixer.music.load(lst[currenttrack])
    pygame.mixer.music.play()

    pygame.mixer.music.set_endevent(NEXT)
    paused = False
    running = True
    while (running and not paused):
        for event in pygame.event.get():

            print ("Play: ", lst[currenttrack])
            if event.type == pygame.QUIT:
                running = False

            elif event.type == NEXT:

                currenttrack = (currenttrack+1) % antall_filer
                print ("Play: ", lst[currenttrack])
                pygame.mixer.music.load(lst[currenttrack])
                pygame.mixer.music.play()

            inp = input("p ?")
            if (inp == "p"):
                pause()

                paused = True
                inp = input("resume? ")
                if (inp =="p"):
                    paused = False
                    pygame.mixer.music.unpause()


pygame.quit()

def pause():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()


def settPause():

    paused = True
    pygame.mixer.music.pause()
    while (paused):
        inpP = input("unpause? ")
        if(inpP == "P"):
            paused = False
            setUnpause()

def settUnpause():
    paused = False
    pygame.mixer.music.unpause()
    #playWorkoutLoop(lst, currenttrack)


main()