import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    drawable = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    asteriods = pygame.sprite.Group()

    AsteroidField.containers = (updateable)
    Asteroid.containers = (drawable, updateable, asteriods)
    Player.containers = (drawable, updateable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    FPS = 60
    game_clock = pygame.time.Clock()
    dt = 0

    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        for sprite in updateable:
            sprite.update(dt)

        dt = game_clock.tick(FPS) / 1000

if __name__ == "__main__":
    main()

