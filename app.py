#! /usr/bin/python3

import os, sys, time

with open(os.devnull, 'w') as f:
    old, sys.stdout = sys.stdout, f
    import pygame
    sys.stdout = old


pygame.init()
pygame.mixer.init()

DISPLAY_WIDTH, DISPLAY_HEIGHT = 1536, 768
CLOCK = pygame.time.Clock()
TICKRATE = 60

class App(object):
    def __init__(self, time):
        self._time = time
        self._display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        self._menu()

    def _load_game(self):
        pass        

    def _menu(self):
        bubbles = []
        self._display.fill((0x1e, 0x2d, 0xff))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
            
            if len(bubbles) <= 16:
                bubbles.append(ambiente.bubble.Bubble())


            CLOCK.tick(TICKRATE)
            pygame.display.update()



if __name__ == "__main__":
    
    t = None
    try:
        with open("resources/timestamp.txt", "r") as timestamp:
            t = float(timestamp.read())
        
        app = App(t)


    except:
        raise

    finally:
        with open("resources/timestamp.txt", "w") as timestamp:
            timestamp.write(str(time.time()))
