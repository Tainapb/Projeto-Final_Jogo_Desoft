# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import os
import random

### -----------------------------Classes ---------------------------------------------------------
class Gelatina(pygame.sprite.Sprite): 
    def __init__(self, img): 
        pygame.sprite.Sprite.__init__(self)
        self.image=img
        self.pulo=False
        self.pos_y_inicial=alt-120  # o 120 posiciona a geleia em cima do chao
        self.rect= self.image.get_rect()
        self.rect.center=(0,alt)   #define a posição de inicio da gelatina
        self.speedy=0
        self.speedx= 0 #velocidade com que se movimenta no eixo x
        
    def pular(self): 
        self.pulo=True
    
    def update(self): 
        self.rect.x+=self.speedx   #acrescenta a velocidade a
        self.speedy+=gravity  
        if self.pulo==True: 
            if self.rect.y<=alt-250:   
                self.pulo= False 
            self.rect.y-=5
        else: 
            if self.rect.y<self.pos_y_inicial: 
                self.rect.y+=5
            else: 
                self.rect.y=self.pos_y_inicial 
        #para manter dentro da tela 
        if self.rect.right> larg: 
            self.rect.right=larg
        if self.rect.left < 0: 
            self.rect.left=0 
           
class Chao(pygame.sprite.Sprite): 
    def __init__(self, imagem): 
        pygame.sprite.Sprite.__init__(self)
        self.image= imagem
        self.rect=self.image.get_rect()
        self.rect = pygame.Rect(0,0,550,50 )
        self.rect.y=alt-50 #posição Y do chão 
        self.rect.x=-40 #posicao x do chão 
    
    def draw(self): 
        window.blit(pygame.transform.flip(self.image, False, False), (self.rect.x - 12, self.rect.y - 5))
        pygame.draw.rect(window, (255,255,255), self.rect, 2)   
    def update(self): 
        if  self.rect.topright[0]<0: 
            self.rect.x=larg
       
class Plataformas(pygame.sprite.Sprite): 
    def __init__(self, imagem, x, y): 
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(imagem, (110,40))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

pygame.init()
x=50
y=20
larg=500
alt=600
gravity=1
# ----- Gera tela principal
window = pygame.display.set_mode((larg,alt))
pygame.display.set_caption('Gelatin Jumping')

#permite acesso as fotos na pasta imagens 
diret=os.path.dirname(__file__)
direct_image=os.path.join(diret,"imagens")

# ----- Inicia estruturas de dados

#imagem de fundo
image_f=pygame.image.load(os.path.join(direct_image,'fundo.jpg')).convert_alpha()
image_fundo=pygame.transform.scale(image_f, (larg, alt))#aplicando a escala para que a imagem seja to tamanho equivalente
#imagem da plataforma
plat_larg=120
plat_alt=50

plat=pygame.image.load(os.path.join(direct_image, 'prato.png')).convert_alpha()
plataforma=pygame.transform.scale(plat, (plat_larg, plat_alt))
plat_x=random.randint(0,alt-plat_larg)#posição x dos pratos
plat_y= random.randint(-100, -plat_alt)
plat_velox=random.randint(-3, 3)
plat_veloy=random.randint(2, 9)
#definindo as dimensões da gelatina e carregando a imagem da gelatina
gel_alt=100
gel_larg=100
gel=pygame.image.load(os.path.join(direct_image, 'geleia.png')).convert_alpha()
geleia=pygame.transform.scale(gel, (gel_larg, gel_alt))
#definindo as dimenssões do Chão carregando a imagem do chão
chao_i=pygame.image.load(os.path.join(direct_image, 'plat.png')).convert_alpha()
chao=pygame.transform.scale(chao_i, (610,70)) #tamanho do chão
#tempo e taxa de fp por segundo 
clock = pygame.time.Clock()
FPS = 60
max=15  #maximo de plataformas que aparecerão na tela 

todas=pygame.sprite.Group()
plataforma_grupo=pygame.sprite.Group()
gelatina=Gelatina(geleia)
todas.add(gelatina)
chao_todas=pygame.sprite.Group()
chao_prin=Chao(chao)
chao_todas.add(chao_prin)

for i in range(max): 
    i_w=random.randint(40,60)
    i_x=random.randint(0,larg-i_w)
    i_y= i* random.randint(80,120)
    plataforma_i= Plataformas(plataforma, i_x, i_y)
    plataforma_grupo.add(plataforma_i)
game = True
# ===== Loop principal =====
while game:

    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if event.type==pygame.KEYDOWN: 
            if event.key ==pygame.K_LEFT: 
                gelatina.speedx-=8
            if event.key ==pygame.K_RIGHT: 
                gelatina.speedx+=8
            if event.key ==pygame.K_SPACE:  
                gelatina.pular()
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT:
                gelatina.speedx += 8
            if event.key == pygame.K_RIGHT:
                gelatina.speedx -= 8

    # ----- Gera saídas
    #hits=pygame.sprite.spritecollide(gelatina, plataforma_grupo, True)
    todas.update()
    hits = pygame.sprite.spritecollide(gelatina, chao_todas,False)
    if len(hits)>0: 
        print("colisão")
        gelatina.pular()
    
    window.fill((200, 0, 100))  # Preenche com a cor branca
    window.blit(image_fundo, (0,0))   #define a imagem de fundo e posiciona para preencher toda a tela 
    window.blit(plataforma, (plat_x, plat_y))
    plataforma_grupo.draw(window)
    chao_todas.draw(window)
    #chao_prin.draw()    #colocar como comentário depois 
    todas.draw(window)
  
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

