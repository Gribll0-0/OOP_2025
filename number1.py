import pygame
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 700))
rect(screen, (255, 255, 255), (0, 0, 800, 700))
circle(screen, (255, 255, 0), (400, 375), 100)
circle(screen, (245, 3, 3), (350, 355), 20)
circle(screen, (0, 0, 0), (350, 360), 10)
circle(screen, (245, 3, 3), (450, 355), 15)
circle(screen, (0, 0, 0), (450, 360), 8)
line(screen, (0, 0, 0), (380, 335), (305, 300), 10)
line(screen, (0, 0, 0), (420, 335), (480, 300), 10)
rect(screen, (0, 0, 0), (350, 400, 100, 25), 20)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()