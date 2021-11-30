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

score=0
lives=3
#titulo
titulo= 'Jelly Jump'
#permite acesso as fotos na pasta imagens 
diret=os.path.dirname(__file__)
direct_imag=os.path.join(diret,"imagens")

logo='jellyjump.png'

#definindo as fontes do texto 
fonte=pygame.font.SysFont("inkfree", 25, bold=True, italic=True )  # vai definir a fonte do texto que aparecerá na tela 
fonte2=pygame.font.SysFont("inkfree", 40, bold=True, italic=True )
fonte3=pygame.font.SysFont("inkfree", 30, bold=True, italic=True )


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


#musica_abertura=
#inicio_tecla=