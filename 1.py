import pygame
from pygame.locals import *
from sys import exit
import os 
import random
pygame.init()
pygame.mixer.init()

diret= os.path.dirname(__file__)
diret_imag= os.path.join(diret, 'imagens')
larg=640
alt=480

#cores
black=(0,0,0)
white=(255,255,255)
rose= (210, 100, 100)

tela=pygame.display.set_mode((larg, alt))
pygame.display.set_caption("Dinossauro") 

sprite= pygame.image.load(os.path.join(diret_imag,"pl.png" )).convert_alpha() #conserva a transparecia
class Dino(pygame.sprite.Sprite): 
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images_dino=[]
        for i in range (3):
            img=sprite.subsurface((i*32,0), (32,32))
            img=pygame.transform.scale(img, (150,150))
            self.images_dino.append(img)
        self.index_lista=0
        self.image=self.images_dino[self.index_lista]
        self.pos_y_inicial=alt-64-128//2
        self.rect=self.image.get_rect()
        self.rect.center=(100,alt-64)
        self.pulo=False
    def pular(self): 
        self.pulo=True

    def update(self): 
        if self.pulo==True: 
            if self.rect.y<=200: 
                self.pulo=False
            self.rect.y-=20
        else: 
            if self.rect.y<self.pos_y_inicial: 
                self.rect.y+=20
            else: 
                self.rect.y=self.pos_y_inicial
        if self.index_lista>2: 
            self.index_lista=0
        self.index_lista+=0.25
        self.image=self.images_dino[int(self.index_lista)]

class Nuvens(pygame.sprite.Sprite): 
    def __init__(self): 
        pygame.sprite.Sprite.__init__(self)
        self.image=sprite.subsurface(( 3*32, 0), (32,32)) 
        self.image=pygame.transform.scale(self.image, (32*3, 32*3))
        self.rect=self.image.get_rect()
        self.rect.y=random.randrange(50,200,50)
        self.rect.x=larg-random.randrange(30,300,90)
    def update(self): #faz ocorrer o movimento 
        if  self.rect.topright[0]<0: 
            self.rect.x=larg
            self.rect.y=random.randrange(50,200,50)
        self.rect.x-=10 #velocidade
class Chao(pygame.sprite.Sprite): 
    def __init__(self, pos_x): 
       pygame.sprite.Sprite.__init__(self)
       self.image=sprite.subsurface((4*32,0), (32,32))
       self.image=pygame.transform.scale(self.image, (32*2, 32*2))
       self.rect=self.image.get_rect()
       self.rect.y=alt-64
       self.rect.x=pos_x*64
    def update(self): 
        if  self.rect.topright[0]<0: 
            self.rect.x=larg
        self.rect.x-=10 #velocidade

todas = pygame.sprite.Group()
dino=Dino()
todas.add(dino)
relog=pygame.time.Clock() #controla a taxa de frames do jogo
for i in range(4): 
    nuvem=Nuvens()
    todas.add(nuvem)
for i in range(larg*10): 
    chao=Chao(i)
    todas.add(chao)
game=True
while game: 
    relog.tick(30)
    tela.fill(rose)
    for event in pygame.event.get(): 
        if event.type==QUIT:
            pygame.quit() #permitindo que se feche a janela
            exit()
        if event.type==KEYDOWN: 
            if event.key==K_SPACE: 
                dino.pular()
    todas.draw(tela)
    todas.update()
    pygame.display.flip()