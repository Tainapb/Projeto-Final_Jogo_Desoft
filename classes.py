import os
import sys
import pygame
from pygame.locals import*
import random
import time
from config import*

#classe da gelatina/jogador principal 
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
    def update(self,x):
        self.rect.y+=-self.energy
        self.energy -=1.1 #impulso que leva a gelatina a cair age como a gravidade
        #chega se não passa da tela 
        if self.rect.right > larg-10: 
            self.rect.right =larg -10
        if self.rect.left<-10: 
            self.rect.left=-10
        if game_over==True: 
            self.kill()
            self.rect.center=(x, alt-120)
    def draw(self):
        tela.blit(pygame.transform.flip(self.image, self.flip, False),(self.rect.x-12, self.rect.y-5))
        pygame.draw.rect(tela,(255,255,255), self.rect, 2)
    def move(self):
        self.delta_y+=self.velocidade_y
#classe que cria o chão para a gelatina não ficar voando antes de iniciar nas plataformas
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
        if self.rect.top>alt or game_over==True: #checa se a plataforma saiu da tela
            self.kill()  # deleta a plataforma da memoria    
    def move(self, delta):
        self.rect.y += delta
#classe das plataformas que será onde a gelatina irá pular
class Plataformas(pygame.sprite.Sprite): 
    def __init__(self, x, y, larg ): 
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(imagem_plataforma,(120,50))
        self.rect=self.image.get_rect()
        self.rect = pygame.Rect(0,0,100,10)
        self.rect.x = x
        self.rect.y = y
        self.flip=False
        if game_over==True: 
            self.kill() 
    def update(self): 
        if self.rect.top>alt: #checa se a plataforma saiu da tela
            self.kill() # deleta a plataforma da memoria    

class Colher(pygame.sprite.Sprite): # classe dos inimigos que retirarão a vida da gelatina 
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.image=pygame.transform.scale(img, (105,105)) #definindo o tamanho da geleia
        self.larg=80  #largura do retângulo
        self.alt=75   #altura do retângulo
        self.rect=pygame.Rect(0,0,self.larg, self.alt) #define o tamanho do retangulo 
        self.rect.x=0 #posição no eixo x
        self.speed=random.randint(0,5)  #sorteando a velocidade com que se movimenta 
        self.rect.y=random.randint(0,larg) #sorteando a posição no eixo x que irão aparecer
        self.rect.center=(self.rect.x,self.rect.y)  #define a posição em que a colher ira aparecer na tela 
    def update(self): 
        self.rect.x += 3
        self.rect.y+=self.speed
        if self.rect.right>larg+50: #checa se a colher saiu 
            self.kill() #deleta a colher caso ela saia da tela 

class Vidas(pygame.sprite.Sprite):  #classe que define a quantidade de vidas da gelatina 
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #criando uma sprite de movimento 
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
           self.kill()  #se o game over acontecer as vidas vão sumir da tela 

plataforma_grupo=pygame.sprite.Group() #cria grupo das plataformas
clock=pygame.time.Clock() #velocidade de processamento
todas =pygame.sprite.Group()


gelatina=Gelatina(larg/2,alt-150) #define a posição que a gelatina vai iniciar o jogo
todas.add(gelatina)


all_colheres=pygame.sprite.Group()
chao=Chao(100,imagem_chao)
game_over=False 
vidas=pygame.sprite.Group()
#criando plataformas iniciais
plataforma_grupo.add(chao)
#Loop principal

for i in range(lives+1):
    cora=Vidas(i*50,50)
    vidas.add(cora)  

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