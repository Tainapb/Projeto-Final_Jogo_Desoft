import os
import sys
import pygame
from pygame.locals import*
import random
JUMP_STEP = 15
def draw_fundo(im_fundo_rol): 
    tela.blit(imagem_fundo, (0,0+im_fundo_rol))
    tela.blit(imagem_fundo, (0,-600+im_fundo_rol))
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
        self.energy -=1
        #chega se não passa da tela 
        if self.rect.right > larg-10: 
            self.rect.right =larg -10
        if self.rect.left<-10: 
            self.rect.left=-10

      
    def draw(self):
        tela.blit(pygame.transform.flip(self.image, self.flip, False),(self.rect.x-12, self.rect.y-5))
        pygame.draw.rect(tela,(255,255,255), self.rect, 2)
    def move(self):
        if self.rect.bottom <plataforma.rect.centery: 
                    if self.velocidade_y>0: 
                        self.rect.bottom=plataforma.rect.top
                        self.delta_y=0
                        self.velocidade_y=-20
                        #som_pulo.play()
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
        self.rect = pygame.Rect(0,0,100,30 )
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
pygame.init()
#cores 
cinza =(127,127,127)
rosa=(200, 0, 100)
#som_pulo = pygame.mixer.Sound('pulo.wav')
#dimensões
larg=450
alt=650
#variaveis 
rol=0    #rolagem
im_fundo_rol=0  #rolagem da imagem de fundo
rolt_t=200   #velocidade de subida do fundo
max=1 #limite de plataformas
#permite acesso as fotos na pasta imagens 
diret=os.path.dirname(__file__)
direct_imag=os.path.join(diret,"imagens")
tela=pygame.display.set_mode((larg, alt)) #criando a tela principal
image_geleia= pygame.image.load(os.path.join(direct_imag, "geleia.png" )).convert_alpha()
pygame.display.set_caption('Gelatin Jumping')
imagem_fundo=pygame.image.load(os.path.join(direct_imag, 'fundo.jpg')).convert() #criando a imagem de fundo
imagem_fundo=pygame.transform.scale(imagem_fundo, (larg, alt))
imagem_chao=pygame.image.load(os.path.join(direct_imag, "plat.png")).convert_alpha()
imagem_plataforma=pygame.image.load(os.path.join(direct_imag,'prato.png')).convert_alpha()
plataforma_grupo=pygame.sprite.Group() #cria grupo das plataformas
clock=pygame.time.Clock() #velocidade de processamento
todas =pygame.sprite.Group()
gelatina=Gelatina(larg/2,alt-150) #define a posição que a gelatina vai iniciar o jogo
todas.add(gelatina)
#criando chão 
chao=Chao(100,imagem_chao)

#criando plataformas iniciais
plataforma_grupo.add(chao)
rol = 0
#Loop principal
while True:
    clock.tick(60) #o jogo não vai rodar mais rapido que 60 FPS por segundo 
    eventos=pygame.event.get() #retorna uma lista com os comandos que o usuário fez no teclado
    for event in eventos: 
        if event.type==pygame.QUIT:
            pygame.quit() #permitindo que se feche a janela
            sys.exit()
            # permitindo movimentação pelo teclado
    # permite a movimentação da geleia pelas setas 
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        gelatina.rect.x += 8 #mudar esse numero se quiser que ela ande mais ou menos rápido
        gelatina.flip = False
    if key[pygame.K_LEFT]:
        gelatina.rect.x -= 8  #mudar esse numero se quiser que ela ande mais ou menos rápido
        gelatina.flip = True
    todas.update() 
  
    # ajusta o limite superior de gelatina
    if gelatina.rect.y < alt // 2:
        gelatina.rect.y = alt // 2
        for obs in plataforma_grupo.sprites():
            obs.rect.y += JUMP_STEP
    hits = pygame.sprite.spritecollide(gelatina,plataforma_grupo,False,pygame.sprite.collide_mask)
    for hit in hits:
        gelatina.jump()
        # chao.rect.y+=10 #atualiza posição vertical da plataforma
        rol = hit.rect.y
    #desenha o fundo
    im_fundo_rol+=rol
    if im_fundo_rol>=600: #altura
        im_fundo_rol=0
    draw_fundo(im_fundo_rol)
    #cria plataformas
    if len(plataforma_grupo)<max+1:
        plat_larg = random.randint(40,60) #30,50 ou 40,60
        plat_x = random.randint(0,larg-plat_larg)
        if len(plataforma_grupo) == 1:
           plat_y = 500    #esse número define a posição em que as plataformas vão começar a aparecer 
        else:
            plat_y = plataforma_grupo.sprites()[-1].rect.y - 150 #esse número define o espaçamento entre as plataformas
        plataforma = Plataformas(plat_x,plat_y,plat_larg)
        plataforma_grupo.add(plataforma)
    #gelatina.move()
    tela.blit(imagem_fundo, (0,0))
    #pygame.draw.line(tela, rosa, (0, rolt_t), (larg,rolt_t))
    plataforma_grupo.draw(tela)
    plataforma_grupo.update() #atualiza plataforma
    todas.draw(tela)
    #gelatina.draw()
    #plataforma.most()
    pygame.display.update()
    #todas.update()
    #pygame.display.flip() #faz a atualização da tela  
'''  
     #gravidade
        self.velocidade_y+=gravi
        self.delta_y+=self.velocidade_y
        #checa se a gelatina não sai da tela
        if self.rect.left +self.delta_x <0: 
            self.delta_x=-self.rect.left
        if self.rect.right +self.delta_x > larg:
            self.delta_x=larg-self.rect.right
        #colisão com o chão
        if self.rect.bottom+self.delta_y> alt: 
            self.delta_y=0
            self.velocidade_y=-20
        #colisão com o topo 
        if self.rect.top<=rolt_t: 
            if self.velocidade_y<0:
                rol=-self.delta_y
        self.rect.x+=self.delta_x
        self.rect.y+=self.delta_y
        self.delta_x=0 # mudança da coordenada x
        self.delta_y=0 #mudança da coordenada y
'''