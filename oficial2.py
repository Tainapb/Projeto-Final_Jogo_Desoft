
import os
import sys
import pygame
from pygame.locals import*
from config import larg, JUMP_STEP, alt, rol, preto, max, im_fundo_rol, pos
import random
import time


# função que irá fazer a atualização de texto na tela
def altera_tela(texto, fonte, t, x,y): 
    image=fonte.render(texto, True, t)
    tela.blit(image, (x,y))
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
        self.image=pygame.transform.scale(img, (105,105)) #definindo o tamanho da geleia
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

pygame.init()
pygame.mixer.init()

#carregando os sons do jogo 
som_pulo = pygame.mixer.Sound('musics/pulo.wav')
som_queda = pygame.mixer.Sound('musics/queda1.wav')
som_colher=pygame.mixer.Sound('musics/colher.wav')
#definindo as fontes do texto 
fonte=pygame.font.SysFont("inkfree", 25, bold=True, italic=True )  # vai definir a fonte do texto que aparecerá na tela 
fonte2=pygame.font.SysFont("inkfree", 40, bold=True, italic=True )
fonte3=pygame.font.SysFont("inkfree", 30, bold=True, italic=True )

  # vai definir a fonte   do texto que aparecerá na tela 
#variaveis 

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

plataforma_grupo=pygame.sprite.Group() #cria grupo das plataformas
clock=pygame.time.Clock() #velocidade de processamento

todas =pygame.sprite.Group()
score=0  #o score começa em zero 
lives=3  #quantidade de vidas 
velo_nova=1
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

game=True

while game:
    clock.tick(60) #o jogo não vai rodar mais rapido que 60 FPS por segundo 
    eventos=pygame.event.get() #retorna uma lista com os comandos que o usuário fez no teclado 
    for event in eventos: 
        if event.type==pygame.QUIT:
            pygame.quit() #permitindo que se feche a janela
            sys.exit()          
    if game_over==False: 
        # permitindo movimentação pelo teclado
        # permite a movimentação da geleia pelas setas 
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            gelatina.rect.x += 8 #mudar esse numero se quiser que ela ande mais ou menos rápido
            gelatina.flip = False
        if key[pygame.K_LEFT]:
            gelatina.rect.x -= 8  #mudar esse numero se quiser que ela ande mais ou menos rápido
            gelatina.flip = True
        # ajusta o limite superior de gelatina
        if gelatina.rect.y < alt // 2:
            gelatina.rect.y = alt // 2
            for obs in plataforma_grupo.sprites():
                obs.rect.y += JUMP_STEP
        
        hits = pygame.sprite.spritecollide(gelatina,plataforma_grupo,False,pygame.sprite.collide_mask)
        for hit in hits:  
            gelatina.jump()
            som_pulo.play()
        
                # chao.rect.y+=10 #atualiza posição vertical da plataforma
            rol = hit.rect.y
        
        #muda a cor do fundo caso ultapasse um certo score 
        if score >50: 
                imagem_fundo=pygame.image.load(os.path.join(direct_imag, 'fundo2.jpg')).convert() #criando a imagem de fundo
                imagem_fundo=pygame.transform.scale(imagem_fundo, (larg, alt))
        if score>100: 
            imagem_fundo=pygame.image.load(os.path.join(direct_imag, 'fundo3.jpg')).convert() #criando a imagem de fundo
            imagem_fundo=pygame.transform.scale(imagem_fundo, (larg, alt))
        if score>200: 
            imagem_fundo=pygame.image.load(os.path.join(direct_imag, 'fundo4.jpg')).convert() #criando a imagem de fundo
            imagem_fundo=pygame.transform.scale(imagem_fundo, (larg, alt))
        #desenha o fundo
        im_fundo_rol+=rol
        if im_fundo_rol>=600: #altura
            im_fundo_rol=0
        draw_fundo(im_fundo_rol)
        #cria plataformas
        if len(plataforma_grupo)<max:
            plat_larg = random.randint(40,60) #30,50 ou 40,60
            plat_x = random.randint(0,larg-plat_larg-60)  #define o intervalo em que a plataforma pode aparecer no eixo x
            if len(plataforma_grupo) == 1:
                plat_y = 500    #esse número define a posição em que as plataformas vão começar a aparecer 
            else:
                plat_y = plataforma_grupo.sprites()[-1].rect.y - 140 #esse número define o espaçamento entre as plataformas
                score+=1
            plataforma = Plataformas(plat_x,plat_y,plat_larg)
            plataforma_grupo.add(plataforma)
        for a in range(50):
            x=random.randrange(0,200,5) 
        if score>=25 and random.randint(1,100)==8:
            if len(all_colheres)==0: 
                colher=Colher(imagem_colher)
                all_colheres.add(colher)
        hits2 = pygame.sprite.spritecollide(gelatina,all_colheres,False,pygame.sprite.collide_mask)
        list=[]

        for hit2 in hits2: 
            list.append(hit2)
            cora.kill()
            som_colher.play()
            lives-=1
            colher.kill()
            vidas.sprites()[0].kill()
        #all_colheres.update()
        cont=f'Score: {score}'
        contador=fonte.render(cont, True, (255,255,255))
        tela.blit(imagem_fundo, (0,0))
        tela.blit(contador, (310,40))
        plataforma_grupo.draw(tela)
        plataforma_grupo.update() #atualiza plataforma
        #all_colheres.draw(tela)
        all_colheres.update()
        if gelatina.rect.bottom >alt+150    or lives ==0:
            game_over=True 
            som_queda.play()
        todas.update()
        all_colheres.draw(tela)
        todas.draw(tela)
        vidas.draw(tela)
        vidas.update()
    else:
        gelatina.kill()

        tela.blit(fundo_fim, (0,0))
        tela.blit(fall1, (150,100))
        altera_tela("GAME OVER!", fonte2, (preto),  95, 280)
        altera_tela(f"Score: {score}", fonte2, (preto),  135, 360)
        altera_tela("Press space to play again", fonte3, (preto),  25, 440)
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            game_over=False
           
   

    #todas.draw(tela)

    pygame.display.update()

    