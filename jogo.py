import os
import sys
import pygame
from pygame.locals import*
import random
import time
JUMP_STEP = 15  #tamanho do pulo

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
    def __init__(self, x, y, larg ):
        self.image=pygame.transform.scale(imagem_colher,(50,50))
        self.rect=self.image.get_rect()
        self.rect = pygame.Rect(0,0,40,40)


pygame.init()
pygame.mixer.init()
#cores 
cinza =(127,127,127)
rosa=(200, 0, 100)
preto=(0,0,0)

#carregando os sons do jogo 
som_pulo = pygame.mixer.Sound('Projeto-final/musics/pulo.wav')

#definindo as fontes do texto 
fonte=pygame.font.SysFont("inkfree", 25, bold=True, italic=True )  # vai definir a fonte do texto que aparecerá na tela 
fonte2=pygame.font.SysFont("inkfree", 40, bold=True, italic=True )
fonte3=pygame.font.SysFont("inkfree", 30, bold=True, italic=True )


#dimensões
larg=450
alt=650
score=0
  # vai definir a fonte do texto que aparecerá na tela 
#variaveis 
rol=0    #rolagem
im_fundo_rol=0  #rolagem da imagem de fundo
rolt_t=200   #velocidade de subida do fundo
max=5#limite de plataformas
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
game=True
while game:
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
        #score+=1
        print("colidiu")
        gelatina.jump()
        som_pulo.play()
        # chao.rect.y+=10 #atualiza posição vertical da plataforma
        rol = hit.rect.y

    #muda a cor do fundo caso ultapasse um certo score 
    if score >100: 
            imagem_fundo=pygame.image.load(os.path.join(direct_imag, 'fundo2.jpg')).convert() #criando a imagem de fundo
            imagem_fundo=pygame.transform.scale(imagem_fundo, (larg, alt))
    if score>150: 
        imagem_fundo=pygame.image.load(os.path.join(direct_imag, 'fundo3.jpg')).convert() #criando a imagem de fundo
        imagem_fundo=pygame.transform.scale(imagem_fundo, (larg, alt))
    if score>500: 
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
            plat_y = plataforma_grupo.sprites()[-1].rect.y - 150 #esse número define o espaçamento entre as plataformas
            score+=1
        plataforma = Plataformas(plat_x,plat_y,plat_larg)
        plataforma_grupo.add(plataforma)
    #gelatina.move()
    
    cont=f'Score: {score}'
    contador=fonte.render(cont, True, (255,255,255))
    tela.blit(imagem_fundo, (0,0))
    tela.blit(contador, (310,40))
    plataforma_grupo.draw(tela)
    plataforma_grupo.update() #atualiza plataforma
    if gelatina.rect.bottom >alt+50:  
        #game=False
        game_over=True 
        tela.blit(fundo_fim, (0,0))
        tela.blit(fall1, (150,100))
        altera_tela("GAME OVER!", fonte2, (preto),  95, 280)
        altera_tela(f"Score: {score}", fonte2, (preto),  135, 360)
        altera_tela("Press space to play again", fonte3, (preto),  25, 440)
         
    

    todas.draw(tela)
 
    pygame.display.update()
  
