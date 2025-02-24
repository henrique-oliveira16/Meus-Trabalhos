# faltou colocar a biblioteca de pygame no pc
import pygame # type: ignore
pygame.init()
pygame.mixer.music.load('Seu áudio aqui')
pygame.mixer.music.play()
pygame.event.wait()