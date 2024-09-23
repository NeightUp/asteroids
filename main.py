import pygame as p
from constants import *

def main():
    p.init()
    screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                return
            
        screen.fill("black")
        p.display.flip()

if __name__ == "__main__":
    main()