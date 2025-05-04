#Tentar depois 
import pygame
pygame.init()
pygame.mixer.music.load(filename='ex022.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()