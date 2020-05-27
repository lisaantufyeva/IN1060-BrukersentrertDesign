import pygame



NEXT = pygame.USEREVENT+1

currenttrack = 0

workout1nivaa1 = ["/share/skolearbeid/media/intro0101.mp3","/share/skolearbeid/media/lyd0101.mp3"]

paused = False



def main():

    playWorkout(workout1nivaa1, currenttrack)

def playWorkout(lst, currenttrack):

    pygame.init()
    pygame.mixer.init(frequency = 48000)



    antall_filer = len(lst)

    pygame.mixer.music.load(lst[currenttrack])
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(NEXT)

    running = True
    #inpP = input("pause? ")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == NEXT:
                currenttrack = (currenttrack+1) % antall_filer
                print ("Play: ", lst[currenttrack])
                pygame.mixer.music.load(lst[currenttrack])
                pygame.mixer.music.play()


pygame.quit()

main()