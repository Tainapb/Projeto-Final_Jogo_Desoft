import os
import sys
import pygame
from pygame.locals import*
import random
import time
from classes import *
from config import*
from jogo import vai
# função que irá fazer a atualização de texto na tela
def altera_tela(texto, fonte, t, x,y): 
    image=fonte.render(texto, True, t)
    tela.blit(image, (x,y))

def draw_fundo(im_fundo_rol): 
    tela.blit(imagem_fundo, (0,0+im_fundo_rol))
    tela.blit(imagem_fundo, (0,-600+im_fundo_rol))

def tela_de_inicio(): #função que cria a tela de inicio 
    tela.blit(fundo_inicio, (0,0)) 
    tela.blit(estrela, (150,100))
    altera_tela("Gelatin Jumping", fonte2, (preto), 50,250)
    altera_tela("Press space to play", fonte3, (preto), 60,400)
    altera_tela("Desenvolvido por:", fonte, (preto), 120,560)
    altera_tela("Use the right and left keys to move", fonte4, (preto), 30,350)
    altera_tela("Tainá Bonfim", fonte4, (preto), 150,595)
    altera_tela("Ana Beatriz Ferreira ", fonte4, (preto), 100,620)
    som_ambiente.play()
    pygame.time.delay(500)
    pygame.display.flip()
    teste =True
    while teste: 
        for event in pygame.event.get(): 
            if event.type==pygame.QUIT: 
                pygame.quit()
            if event.type==pygame.KEYUP: 
                if event.key==K_SPACE: 
                    teste=False 
                    som_ambiente.stop()
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        vai==False
        game_over==False 

def tela_over():   #função que cria a tela de game over 
    tela.blit(fundo_fim, (0,0))  
    tela.blit(fall1, (150,100))
    altera_tela("GAME OVER!", fonte2, (preto),  95, 280)
    altera_tela(f"Score: {score}", fonte2, (preto),  125, 360)
    altera_tela("Press space to play again", fonte3, (preto),  25, 440)
    pygame.time.delay(500)
    pygame.display.flip()
    aguardando =True
    while aguardando: 
        for event in pygame.event.get(): 
            if event.type==pygame.QUIT: 
                pygame.quit()
            if event.type==pygame.KEYUP: 
                if event.key==K_SPACE: 
                    aguardando=False 
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        game_over==False