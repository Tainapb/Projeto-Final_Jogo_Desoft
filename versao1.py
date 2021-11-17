import os
import sys
import pygame  
from pygame.locals import*
pygame.init()
#cores 
cinza =(127,127,127)
rosa=(200, 0, 100)
#dimensões
larg=640
alt=500
pos=100
velo=0.3

tela=pygame.display.set_mode((larg, alt)) #criando a tela principal
arq=os.path.join("imagens", "geleia.png") #criando a geleia
imag=pygame.image.load(arq)
imag=pygame.transform.scale(imag, (120,100)) #estabelecendo o tamanho da geleia
imagem_fundo=pygame.image.load('fundo.jpg').convert() #criando a imagem de fundo
imagem_fundo=pygame.transform.scale(imagem_fundo, (larg, alt))
clock=pygame.time.Clock() #velocidade de processamento
y=alt-90
while True:
    delta_time=clock.tick(60) #o jogo não vai rodar mais rapido que 60 FPS por segundo 
    eventos=pygame.event.get() #retorna uma lista com os comandos que o usuário fez no teclado
    for event in eventos: 
        if event.type==pygame.QUIT:
            pygame.quit() #permitindo que se feche a janela
            sys.exit()
        # permitindo movimentação pelo teclado
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w: 
                y=y-20
            if event.key==pygame.K_s:
                y=y+20 
            if event.key==pygame.K_SPACE: 
                print("pular")   
    pos+=velo*delta_time
      #vai fazer a imagem voltar a tela
    if pos > tela.get_width()-imag.get_width():   #faz a imagem bater e voltar   
        velo = -velo
        pos=tela.get_width()-imag.get_width()
    if pos <0: 
        velo= -velo  #faz a imagem bater e voltar sempre
        pos=0

    tela.blit(imagem_fundo, (0,0))
    tela.blit(imag, (pos,y)) #o pos aqui definido irá dar o movimento #define a posição da geleia na tela 
    pygame.display.flip() #faz a atualização da tela 
