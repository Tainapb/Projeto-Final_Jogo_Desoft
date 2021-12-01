import os
import sys
import pygame
from pygame.locals import*
import random
import time

JUMP_STEP = 15  #tamanho do pulo
#cores 
cinza =(127,127,127)
rosa=(200, 0, 100)
preto=(0,0,0)
#dimensões
larg=450
alt=650
score=0 #score inicial 
lives=3 #quantidade de vidas 
rol=0    #rolagem
im_fundo_rol=0  #rolagem da imagem de fundo
rolt_t=200   #velocidade de subida do fundo
max=5#limite de plataformas
pos=100  #posiçaõ inicial 
velo_nova=1
#carregando os sons do jogo 
som_pulo = pygame.mixer.Sound('musics/pulo.wav')
som_queda = pygame.mixer.Sound('musics/queda1.wav')
som_colher=pygame.mixer.Sound('musics/colher.wav')
som_ambiente=pygame.mixer.Sound('musics/ambiente.mp3')
#definindo as fontes do texto 
fonte=pygame.font.SysFont("inkfree", 25, bold=True, italic=True )  # vai definir a fonte do texto que aparecerá na tela 
fonte2=pygame.font.SysFont("inkfree", 40, bold=True, italic=True )
fonte3=pygame.font.SysFont("inkfree", 30, bold=True, italic=True )
fonte4=pygame.font.SysFont("inkfree", 20, bold=True, italic=True )
 
#permite acesso as fotos na pasta imagens 
diret=os.path.dirname(__file__)
direct_imag=os.path.join(diret,"imagens")
#carrengando as sprites que serão utilizadas no jogo
tela=pygame.display.set_mode((larg, alt)) #criando a tela principal
image_geleia= pygame.image.load(os.path.join(direct_imag, "geleia.png" )).convert_alpha()
pygame.display.set_caption('Gelatin Jumping')
fall=pygame.image.load(os.path.join(direct_imag, "fall2.png" )).convert_alpha()
fall1=pygame.transform.scale(fall, (150,150))   #gelatina de cabeça para baixo
fundo_f= pygame.image.load(os.path.join(direct_imag, "fim.jpg" )).convert_alpha()
fundo_fim=pygame.transform.scale(fundo_f, (larg, alt))
imagem_fundo=pygame.image.load(os.path.join(direct_imag, 'fundo.jpg')).convert() #criando a imagem de fundo
imagem_fundo=pygame.transform.scale(imagem_fundo, (larg, alt))
imagem_chao=pygame.image.load(os.path.join(direct_imag, "plat.png")).convert_alpha()
imagem_colher=pygame.image.load(os.path.join(direct_imag, "colher.png")).convert_alpha()
imagem_plataforma=pygame.image.load(os.path.join(direct_imag,'prato.png')).convert_alpha()
coracoes=pygame.image.load(os.path.join(direct_imag, 'coracoes.png'))
fundo_i= pygame.image.load(os.path.join(direct_imag, "inicio.jpg" )).convert_alpha()
estre= pygame.image.load(os.path.join(direct_imag, "teste.png" )).convert_alpha()
estrela = pygame.transform.scale(estre, (150,120))
fundo_inicio=pygame.transform.scale(fundo_i, (larg, alt))

vai=True