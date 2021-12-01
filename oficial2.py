import os
import sys
import pygame
from pygame.locals import*
import random
import time

# função que irá fazer a atualização de texto na tela
def altera_tela(texto, fonte, t, x,y): 
    image=fonte.render(texto, True, t)
    tela.blit(image, (x,y))

#classe da gelatina/jogador principal 
class Gelatina(pygame.sprite.Sprite): 
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        #self.image=pygame.transform.scale(image_geleia, (100,100)) #definindo o tamanho da geleia
        self.images=[]  #lista em que será armazenda as fotos que darão a sensação de movimento
        self.images.append(pygame.image.load('imagens/geleia2.png')) #chamando as imagens 
        self.images.append(pygame.image.load('imagens/geleia1.png'))
        self.images.append(pygame.image.load('imagens/geleia3.png'))
        self.atual=0   #será utilizada para controlar o index da lista
        self.image=self.images[self.atual]   #definindo a imagem que irá começar 
        self.image=pygame.transform.scale(self.image,(100,100))  #definido o tamanho das imagens 
        self.rect=self.image.get_rect()  #chamando o retangulo 
        self.velocidade_y=0  #definição da velocidade 
        self.delta_x = 0
        self.delta_y =0
        self.jump()  #chamando o pulo 
    def jump(self):
        self.energy = JUMP_STEP  #definindo o puolo
    def update(self):
        self.rect.y+=-self.energy
        self.energy -=1.1 #impulso que leva a gelatina a cair age como a gravidade
        self.atual+=0.05  #adicionando a taxa com que as imagens vão ser atualizadas
        if self.atual>=len(self.images):   #se ultrapassar o numero de imagens disponpiveis na lista volta a ser zero
            self.atual=0
        self.image=self.images[int(self.atual)]   #denine a parte inteira do index que esta chamando a imagem na lista
        #chega se não passa da tela 
        if self.rect.right > larg-10: 
            self.rect.right =larg -10
        if self.rect.left<-10: 
            self.rect.left=-10
        if game_over==True:   #se o game over aparecer a gelatina é deletada  
            self.kill()
            
    def draw(self):  #
        tela.blit(pygame.transform.flip(self.image, self.flip, False),(self.rect.x-12, self.rect.y-5))
        pygame.draw.rect(tela,(255,255,255), self.rect, 2)
    def move(self):   #define a movimentação da gelatina 
        self.delta_y+=self.velocidade_y
#classe que cria o chão para a gelatina não ficar voando antes de iniciar nas plataformas
class Chao(pygame.sprite.Sprite): 
    def __init__(self, posicao_x, imagem): 
        pygame.sprite.Sprite.__init__(self)
        self.image= imagem
        self.image=pygame.transform.scale(self.image, (610,70)) #definido o tamanho do chão
        self.rect=self.image.get_rect()
        self.rect.y=alt-40 #posição Y do chão 
        self.rect.x=-40#posicao x do chão 
    def update(self): #faz a atualização
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
        self.image=pygame.transform.scale(imagem_plataforma,(120,50)) #definido o tamanho das plataformas 
        self.rect=self.image.get_rect()
        self.rect = pygame.Rect(0,0,100,10)  #definindo a posição que aparecerá na tela 
        self.rect.x = x
        self.rect.y = y
        if game_over==True: 
            self.kill() 
    def update(self): #faz a atualização 
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
    def update(self): #faz a atualização 
        self.rect.x += 3  #faz a gelatina atravessar a tela no eixo x 
        self.rect.y+=self.speed  #faz a atgualixação da velocidade da colher no eixo y 
        if self.rect.right>larg+50: #checa se a colher saiu 
            self.kill() #deleta a colher caso ela saia da tela 

class Vidas(pygame.sprite.Sprite):  #classe que define a quantidade de vidas da gelatina 
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #criando uma sprite de movimento 
        self.list=[]  #lista em que serão adicionadas as imagens para dar a sensação de movimento 
        for i in range(3): 
            img=coracoes.subsurface((i*32,0), (32,32))   #chamando as imagens que estão em uma unica sprite mas em posições diferentes 
            img=pygame.transform.scale(img, (120,120)) #definindo o tamanho das imagens 
            self.list.append(img)
        self.index_lista=0  #index da lista
        self.image=self.list[self.index_lista] #definindo a primeira imagem 
        self.rect=self.image.get_rect()  #chamando o retângulo 
        self.rect.center= (x,y)   #estabelecendo a posição que irá aparecer na tela 
    def update(self):  #faz a atualização 
        if self.index_lista>2: 
            self.index_lista=0
        self.index_lista+=0.25  #define a velocidade do movimento das imagens 
        self.image=self.list[int(self.index_lista)] 
        if game_over==True: 
           self.kill()  #se o game over acontecer as vidas vão sumir da tela 
def tela_over():   #função que cria a tela de game over 
    tela.blit(fundo_fim, (0,0))  #definindo a imagem de fundo 
    tela.blit(fall1, (150,100))   #desenhando a gelatina "morta" na tela
    #escrevendo na tela de game over 
    altera_tela("GAME OVER!", fonte2, (preto),  95, 280)
    altera_tela(f"Score: {score}", fonte2, (preto),  125, 360)
    altera_tela("Press space to play again", fonte3, (preto),  25, 440)
    pygame.time.delay(500)   #delay para sair da tela de game over
    pygame.display.flip()
    aguardando =True
    while aguardando: 
        #permite que a pessoa feche a janela 
        for event in pygame.event.get(): 
            if event.type==pygame.QUIT: 
                pygame.quit()
            if event.type==pygame.KEYUP: 
                if event.key==K_SPACE: 
                    aguardando=False 
    #se a tecla espaço for pressionada a tela de game over desaparece 
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        game_over==False

def tela_de_inicio(): #função que cria a tela de inicio 
    tela.blit(fundo_inicio, (0,0))  #definindo a imagem de fundo 
    tela.blit(image_geleia, (150,100)) #desenhando a gelatinana tela
    #escrevendo na tela de inicio
    altera_tela("Gelatin Jumping", fonte2, (preto), 50,250)
    altera_tela("Press space to play", fonte3, (preto), 60,400)
    altera_tela("Desenvolvido por:", fonte, (preto), 120,560)
    altera_tela("To move use the right and left keys", fonte4, (preto), 30,350)
    altera_tela("Tainá Bonfim", fonte4, (preto), 150,595)
    altera_tela("Ana Beatriz Ferreira ", fonte4, (preto), 100,620)
    som_ambiente.play()  #faz tocar a música de inicio
    pygame.time.delay(500) #delay para sair da tela de inicio
    pygame.display.flip()
    teste =True
    while teste: 
        #permite que a pessoa feche a janela 
        for event in pygame.event.get(): 
            if event.type==pygame.QUIT: 
                pygame.quit()
            if event.type==pygame.KEYUP: 
                if event.key==K_SPACE: 
                    teste=False 
                    som_ambiente.stop()
    #se a tecla espaço for pressionada a tela de inicio desaparece 
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        vai==False
        game_over==False 
        
pygame.init()
pygame.mixer.init()

JUMP_STEP = 15  #tamanho do pulo
#cores 
cinza =(127,127,127)
rosa=(200, 0, 100)
preto=(0,0,0)
#dimensões
larg=450 #largura 
alt=650 #altura 
score=0 #score inicial 
lives=3 #quantidade de vidas 
rolt_t=200  #velocidade de subida do fundo
max=5 #limite de plataformas
pos=100  #posiçaõ inicial 
velo_nova=1
#carregando os sons do jogo 
som_pulo = pygame.mixer.Sound('musics/pulo.wav')
som_queda = pygame.mixer.Sound('musics/queda1.wav')
som_colher=pygame.mixer.Sound('musics/colher.wav')
som_ambiente=pygame.mixer.Sound('musics/ambiente.mp3')
#definindo as fontes do texto 
fonte=pygame.font.SysFont("inkfree", 25, bold=True, italic=True )  # vai definir a fonte do texto que aparecerá na tela 
fonte2=pygame.font.SysFont("inkfree", 40, bold=True, italic=True )
fonte3=pygame.font.SysFont("inkfree", 30, bold=True, italic=True )
fonte4=pygame.font.SysFont("inkfree", 20, bold=True, italic=True )
 
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
fundo_i= pygame.image.load(os.path.join(direct_imag, "inicio.jpg" )).convert_alpha()
fundo_inicio=pygame.transform.scale(fundo_i, (larg, alt))
gelatin=pygame.image.load(os.path.join(direct_imag, 'g2.png'))
plataforma_grupo=pygame.sprite.Group() #cria grupo das plataformas
clock=pygame.time.Clock() #velocidade de processamento

todas =pygame.sprite.Group()  #grupo que armazena algumas sprites 

gelatina=Gelatina(larg/2,alt-150) #define a posição que a gelatina vai iniciar o jogo
todas.add(gelatina)
all_colheres=pygame.sprite.Group() #grupo que armazena as colheres 
chao=Chao(100,imagem_chao)
game_over=False 
vidas=pygame.sprite.Group() #grupo que armazena as vidas 
#criando plataformas iniciais
plataforma_grupo.add(chao)
#Loop principal

for i in range(lives+1):
    cora=Vidas(i*50,50)
    vidas.add(cora)  
tela_de_inicio()  #chamando a tela de inicio 
game=True
vai =True   #define se o jogo deve se iniciar 
while game:
    clock.tick(60) #o jogo não vai rodar mais rapido que 60 FPS por segundo 
    eventos=pygame.event.get() #retorna uma lista com os comandos que o usuário fez no teclado 
    if vai ==True: 
        for event in eventos: 
            if event.type==pygame.QUIT:
                pygame.quit() #permitindo que se feche a janela
                sys.exit()          
        if game_over==False: 
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
            #verifica se houve colisão da gelatina com as plataformas 
            hits = pygame.sprite.spritecollide(gelatina,plataforma_grupo,False,pygame.sprite.collide_mask)
            for hit in hits:  
                gelatina.jump()   #faz a gelatina pular se a colisão acontecer 
                som_pulo.play()  #faz a musica de pulo tocar 

            #muda a cor do fundo caso ultapasse um certo score 
            if score >50: 
                    imagem_fundo=pygame.image.load(os.path.join(direct_imag, 'fundo2.jpg')).convert() #criando a imagem de fundo
                    imagem_fundo=pygame.transform.scale(imagem_fundo, (larg, alt))
            if score>100: 
                imagem_fundo=pygame.image.load(os.path.join(direct_imag, 'fundo3.jpg')).convert() #criando a imagem de fundo
                imagem_fundo=pygame.transform.scale(imagem_fundo, (larg, alt))
            if score>150: 
                imagem_fundo=pygame.image.load(os.path.join(direct_imag, 'fundo4.jpg')).convert() #criando a imagem de fundo
                imagem_fundo=pygame.transform.scale(imagem_fundo, (larg, alt))
    
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
            if score>=25 and random.randint(1,100)==8:  #defindo quando as colheres podem começar a aparecer 
                if len(all_colheres)==0: 
                    colher=Colher(imagem_colher)
                    all_colheres.add(colher)

            #verifica a colisão entre a gelatina e as colheres 
            hits2 = pygame.sprite.spritecollide(gelatina,all_colheres,False,pygame.sprite.collide_mask)
            list=[]  #cria uma lista que irá informar a quantidade de vezes que ocorre a colisão 
            for hit2 in hits2: 
                list.append(hit2)
                cora.kill()
                som_colher.play()
                lives-=1 #se ocorrer a colisão 1 é descontado na quantidade de vidas 
                colher.kill()  #a colher que sofreu a colisão é deletada instantaneamente 
                vidas.sprites()[0].kill()   #elimina os corações em caso de colisão 
            #all_colheres.update()
            cont=f'Score: {score}'   
            contador=fonte.render(cont, True, (255,255,255)) #define a fonte do score 
            tela.blit(imagem_fundo, (0,0)) #coloca uma imagem de fundo 
            tela.blit(contador, (310,40)) #mostra o score na tela
            plataforma_grupo.draw(tela)
            plataforma_grupo.update() #atualiza plataforma
            #all_colheres.draw(tela)
            all_colheres.update()
            if gelatina.rect.bottom >alt+150    or lives ==0:  #se a gelatina sair da tela ou a quantidade de vidas for igual a zero 
                game_over=True #a tela de game over aparece 
                som_queda.play()  #dispara o som de queda 
            todas.update() #faz a atualização das sprites dentro desse grupo 
            all_colheres.draw(tela)  #faz as colheres aparecerem na tela 
            todas.draw(tela) #faz a gelatina aparecer na tela 
            vidas.draw(tela) #faz as vidas aparecerem na tela 
            vidas.update() #faz a atualização das vidas 
        else:
            tela_over()  #faz a tela de game over aparecer
            #reseta as variaveis e chama os grupos novamente 
            score=0
            lives=3
            velo_nova=1
            todas =pygame.sprite.Group()
            plataforma_grupo=pygame.sprite.Group()
            gelatina=Gelatina(larg/2,alt-150) 
            todas.add(gelatina)
            all_colheres=pygame.sprite.Group()
            chao=Chao(100,imagem_chao)
            plataforma_grupo.add(chao)
            chao=Chao(100,imagem_chao)
            vidas=pygame.sprite.Group()
            plataforma_grupo.add(chao)
            for i in range(lives+1):
                cora=Vidas(i*50,50)
                vidas.add(cora)  
            imagem_fundo=pygame.image.load(os.path.join(direct_imag, 'fundo.jpg')).convert() #criando a imagem de fundo
            imagem_fundo=pygame.transform.scale(imagem_fundo, (larg, alt)) #estabelecendo o tamanho da imagem de fundo 
            game_over=False

    pygame.display.update()

    