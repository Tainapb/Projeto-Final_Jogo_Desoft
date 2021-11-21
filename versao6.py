import os
import sys
import pygame
from pygame.locals import*
import random
class Gelatina(pygame.sprite.Sprite): 
    def __init__(self,imagem,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(image_geleia, (120,100)) #definindo o tamanho da geleia
        self.rect=pygame.Rect(0,0,80,80) #define o tamanho do retangulo 
        self.rect.center=(x,y)  #define a posição em que a gelatina aparecerar na tela
        self.velocidade_y=0

    def move(self): 
        delta_x=0 # mudança da coordenada x
        delta_y=0 #mudança da coordenada y

        # permite a movimentação da geleia pelas setas 
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            delta_x = +10 #mudar esse numero se quiser que ela ande mais ou menos rápido
            self.flip = True
        if key[pygame.K_LEFT]:
            delta_x = -10  #mudar esse numero se quiser que ela ande mais ou menos rápido
          #  self.flip = False
           
        #gravidade
        self.velocidade_y+=gravi
        delta_y+=self.velocidade_y

        #checa se a gelatina não sai da tela
        if self.rect.left +delta_x <0: 
            delta_x=-self.rect.left
        if self.rect.right +delta_x > larg:
            delta_x=larg-self.rect.right
        #checa colisão com o chão/ nao deixa a gelatina passar a tela 
        for plataforma in plataforma_grupo: 
             if plataforma.rect.colliderect(self.rect.x, self.rect.y +delta_y, 110,100): 
                 if self.rect.bottom <plataforma.rect.centery: 
                     if self.velocidade_y>0: 
                         self.rect.bottom=plataforma.rect.top
                         delta_y=0
                         self.velocidade_y=-20
        
        if self.rect.bottom+delta_y> alt: 
            delta_y=0
            self.velocidade_y=-20
        
        
        self.rect.x+=delta_x
        self.rect.y+=delta_y
 
    def draw(self):
        tela.blit(self.image, (self.rect.x-30, self.rect.y-5))
        pygame.draw.rect(tela,(255,255,255), self.rect, 2)
    

class Chao(pygame.sprite.Sprite): 
    def __init__(self, posicao_x, imagem): 
        pygame.sprite.Sprite.__init__(self)
        self.image= imagem
        self.image=pygame.transform.scale(self.image, (610,70)) #tamanho do chão
        self.rect=self.image.get_rect()
        self.rect.y=alt-50 #posição Y do chão 
        self.rect.x=-40#posicao x do chão 
    def update(self): 
        if  self.rect.topright[0]<0: 
            self.rect.x=larg
        #self.rect.x-=5 #velocidade

class Plataformas(pygame.sprite.Sprite): 
    def __init__(self, x, y, larg ): 
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(imagem_plataforma,(150,100))
        self.rect=self.image.get_rect()
        self.rect.x= x
        self.rect.y= y

pygame.init()

#cores 
cinza =(127,127,127)
rosa=(200, 0, 100)
gravi=1
#dimensões
larg=500
alt=600
max=10
#permite acesso as fotos na pasta imagens 
diret=os.path.dirname(__file__)
direct_imag=os.path.join(diret,"imagens")

tela=pygame.display.set_mode((larg, alt)) #criando a tela principal
image_geleia= pygame.image.load(os.path.join(direct_imag, "geleia.png" )).convert_alpha()
pygame.display.set_caption('Gelatin Jumping')
imagem_fundo=pygame.image.load(os.path.join(direct_imag, 'fundo.jpg')).convert() #criando a imagem de fundo
imagem_fundo=pygame.transform.scale(imagem_fundo, (larg, alt))
imagem_chao=pygame.image.load(os.path.join(direct_imag, "plat.png")).convert_alpha()
imagem_plataforma=pygame.image.load(os.path.join(direct_imag,'plataforma1.png')).convert_alpha()
plataforma_grupo=pygame.sprite.Group()
clock=pygame.time.Clock() #velocidade de processamento
todas =pygame.sprite.Group()

gelatina=Gelatina(image_geleia,larg//2,alt-180) #define a posição que a gelatina vai iniciar o jogo
todas.add(gelatina)

#criando chão 
chao=Chao(100,imagem_chao)
todas.add(chao)


for i in range(7): 
    i_w=random.randint(100,150)
    i_x=random.randint(0,larg-i_w)
    i_y= i* random.randint(80,120)
    plataforma= Plataformas(i_x, i_y, i_w)
    plataforma_grupo.add(plataforma)
#Loop principal
while True:
    delta_time=clock.tick(60) #o jogo não vai rodar mais rapido que 60 FPS por segundo 
    eventos=pygame.event.get() #retorna uma lista com os comandos que o usuário fez no teclado
    for event in eventos: 
        if event.type==pygame.QUIT:
            pygame.quit() #permitindo que se feche a janela
            sys.exit()
            # permitindo movimentação pelo teclado
    
    gelatina.move()
    tela.blit(imagem_fundo, (0,0))
    todas.draw(tela)
    plataforma_grupo.draw(tela)
    
    pygame.display.update() 
    #todas.update()
    
   

    #pygame.display.flip() #faz a atualização da tela 