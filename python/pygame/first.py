#!/usr/bin/python
import pygame

pygame.init()

gameDispay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Slither")
pygame.display.update()

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            pass

pygame.quit()
quit()
