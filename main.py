import pygame
import sys
from constants import *
from player import *
from astroid import *
from astroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    astroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Astroid.containers = (updatable, drawable, astroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    af = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for u in updatable:
            u.update(dt)

        screen.fill("black")
        for a in astroids:
            if a.collision(ship):
                print("Game over!")
                sys.exit()
            for b in shots:
                if a.collision(b):
                    a.split()
                    b.kill()
                    
        for d in drawable:
            d.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()