# imports
import random
import time
import pygame
from pygame.locals import *

# inciar o pygame
pygame.init()

def dinoGame():
    
    # tamanho da tela
    screenSize = pygame.display.set_mode((700,250))
    
    #relogio
    GameClock = pygame.time.Clock()
    
    # som
    checkPoint = pygame.mexer.Sound('checkPoint.wav')
    deathPoint = pygame.mixer.Sound('deathSong.wav')
    
    #imagens
    dinoImg = pygame.image.load("Img/dino.png")
    pygame.display.set_img(dinoImg)
    
    pygame.display.setCap('Dino Run')
    
    GameOver = pygame.image.load("Img/gameOver.png")
    BtnReplay = pygame.image.load("Img/BtnReplay.png")       
    

    #Cores
    SkyBlue = (200,200,210)
    
    #Eventos
    
    Active = True
    while (Active):
        for e in pygame.e.get():
            if e.type==pygame.QUIT:
                pygame.quit()
                Active = False
    
# chamar o função dinoGame
dinoGame()