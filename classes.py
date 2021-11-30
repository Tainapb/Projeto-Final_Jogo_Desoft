import os
import sys
import pygame
from pygame.locals import*
import random
import time
from constantes import JUMP_STEP, larg, alt , image_geleia,tela,imagem_plataforma,coracoes

game_over=False 


class Gelatina(pygame.sprite.Sprite): 
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(image_geleia, (100,100)) #definindo o tamanho da geleia
        self.larg=80
        self.alt=75
        self.rect=pygame.Rect(0,0,self.larg, self.alt) #define o tamanho do retangulo 
        self.rect.center=(x,y)  #define a posição em que a gelatina aparecerar na tela
        self.velocidade_y=0
        self.flip = False
        self.delta_x = 0
        self.delta_y =0
        self.jump()
    def jump(self):
        self.energy = JUMP_STEP
    def update(self):
        self.rect.y+=-self.energy
        self.energy -=1.1 #impulso que leva a gelatina a cair age como a gravidade
        #chega se não passa da tela 
        if self.rect.right > larg-10: 
            self.rect.right =larg -10
        if self.rect.left<-10: 
            self.rect.left=-10
        if game_over==True: 
            self.kill()
    def draw(self):
        tela.blit(pygame.transform.flip(self.image, self.flip, False),(self.rect.x-12, self.rect.y-5))
        pygame.draw.rect(tela,(255,255,255), self.rect, 2)
    def move(self):
        self.delta_y+=self.velocidade_y
class Chao(pygame.sprite.Sprite): 
    def __init__(self, posicao_x, imagem): 
        pygame.sprite.Sprite.__init__(self)
        self.image= imagem
        self.image=pygame.transform.scale(self.image, (610,70)) #tamanho do chão
        self.rect=self.image.get_rect()
        self.rect.y=alt-40 #posição Y do chão 
        self.rect.x=-40#posicao x do chão 
    def update(self): 
        if  self.rect.topright[0]<0: 
            self.rect.x=larg
        if self.rect.top>alt: #checa se a plataforma saiu da tela
            self.kill()  # deleta a plataforma da memoria    
    def move(self, delta):
        self.rect.y += delta
class Plataformas(pygame.sprite.Sprite): 
    def __init__(self, x, y, larg ): 
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(imagem_plataforma,(120,50))
        self.rect=self.image.get_rect()
        self.rect = pygame.Rect(0,0,100,10)
        self.rect.x = x
        self.rect.y = y
        self.flip=False
    def update(self): 
        if self.rect.top>alt: #checa se a plataforma saiu da tela
            self.kill()  # deleta a plataforma da memoria    
    def most(self):
        tela.blit(pygame.transform.flip(self.image, self.flip, False),(self.rect.x-12, self.rect.y-5))
        pygame.draw.rect(tela,(255,255,255), self.rect, 2)    
    #def draw(self):
    #    tela.blit(pygame.transform.flip(self.image, self.flip, False),(self.rect.x-12, self.rect.y-5))
    #    pygame.draw.rect(tela,(255,255,255), self.rect, 2)    
class Colher(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.image=pygame.transform.scale(img, (100,100)) #definindo o tamanho da geleia
        self.larg=80
        self.alt=75
        self.rect=pygame.Rect(0,0,self.larg, self.alt) #define o tamanho do retangulo 
        self.rect.x=0
        self.speed=4  #velocidade com que se movimenta 
        self.rect.y=random.randint(0,larg)
        self.rect.center=(self.rect.x,self.rect.y)  #define a posição em que a colher ira aparecer na tela 
    def update(self): 
        self.rect.x += 3
        self.rect.y+=self.speed
        if self.rect.right>larg+50: #checa se a colher saiu 
            self.kill()
class Vidas(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.list=[]
        for i in range(3): 
            img=coracoes.subsurface((i*32,0), (32,32))
            img=pygame.transform.scale(img, (120,120))
            self.list.append(img)
        self.index_lista=0
        self.image=self.list[self.index_lista]
        self.rect=self.image.get_rect()
        self.rect.center= (x,y)
    def update(self): 
        if self.index_lista>2: 
            self.index_lista=0
        self.index_lista+=0.25
        self.image=self.list[int(self.index_lista)] 
        if game_over==True: 
           self.kill()