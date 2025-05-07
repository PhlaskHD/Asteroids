import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    AsteroidField.containers = (updatable,)
    Asteroid.containers = (updatable, drawable, asteroids_group)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shot_group)

    asteroid_field = AsteroidField()
    
    print(asteroids_group.sprites())
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)


        for each in asteroids_group:
            if each.is_colliding(player) == True:
                print("Game over!")
                sys.exit()

        for asteroid in asteroids_group:
            for shot in shot_group:
                if asteroid.is_colliding(shot):
                    asteroid.split()
                    shot.kill()


        screen.fill("black")

        for each in drawable:
            each.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()