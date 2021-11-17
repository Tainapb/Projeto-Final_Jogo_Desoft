import os
import sys
import pygame  
from pygame.locals import*
class Gelatina(pygame.sprite.Sprite): 
    def __init__(self,imagem):
        pygame.sprite.Sprite.__init__(self)
        self.pos_y_inicial= alt-90 #referencia        
        self.pulo=False
        self.image=imagem 
        self.image=pygame.transform.scale(imagem, (120,100))
        self.rect=self.image.get_rect()
        self.rect.center=(y,100)
    def pular (self): 
        self.pulo=True
    
    def update (self): 
        if self.pulo==True: 
            if self.rect.y<=420:
                self.pulo= False 
            self.rect.y-=5
        else: 
            if self.rect.y<self.pos_y_inicial: 
                self.rect.y+=5
            else: 
                self.rect.y=self.pos_y_inicial
                
class Chao(): 
    def __init__(self): 
        12
pygame.init()

#cores 
cinza =(127,127,127)
rosa=(200, 0, 100)

#dimensões
larg=500
alt=600
diret=os.path.dirname(__file__)
direct_imag=os.path.join(diret,"imagens")

tela=pygame.display.set_mode((larg, alt)) #criando a tela principal
image_geleia= pygame.image.load(os.path.join(direct_imag, "geleia.png" )).convert_alpha()
imagem_fundo=pygame.image.load('fundo.jpg').convert() #criando a imagem de fundo
imagem_fundo=pygame.transform.scale(imagem_fundo, (larg, alt))
clock=pygame.time.Clock() #velocidade de processamento
y=38

todas =pygame.sprite.Group()
gelatina=Gelatina(image_geleia)
todas.add(gelatina)
        
while True:
    delta_time=clock.tick(60) #o jogo não vai rodar mais rapido que 60 FPS por segundo 
    eventos=pygame.event.get() #retorna uma lista com os comandos que o usuário fez no teclado
    for event in eventos: 
        if event.type==pygame.QUIT:
            pygame.quit() #permitindo que se feche a janela
            sys.exit()
            # permitindo movimentação pelo teclado
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT: 
                y=y+50
                print('direita')
            if event.key==pygame.K_LEFT:
                print('esquerda') 
            if event.key==pygame.K_SPACE: 
                gelatina.pular()
    tela.blit(imagem_fundo, (0,0))
    todas.draw(tela)
    todas.update()
    
    pygame.display.flip() #faz a atualização da tela 

