import os
import sys
import pygame
import random
import time
import constantes
import sprites

class Game:
    def __init__(self):
        #criando tela 
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode(450,650)
        pygame.display.set_caption(constantes.titulo)
        self.clock = pygame.time.Clock()
        self.rodando = True
        self.font=pygame.font.match_font(constantes.fonte)
        self.carregar_arquivos()

    def jogo_novo(self):
        #instancia as classes das sprites
        self.todas_sprites = pygame.sprite.Group()
        self.rodar()

    def rodar(self):
        #loop do jogo
        self.game = True
        while self.game:
            self.clock.tick(60)
            self.events()
            self.update_sprites()
            self.draw_sprites()

    def events(self):
        #define eventos
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                if self.game:
                    self.game= False
                self.rodando=False

    def update_sprites(self):
        self.todas_sprites.update()

    def draw_sprites(self):
        self.tela.fill(constantes.preto)
        self.todas_sprites.draw(self.tela)
        pygame.display.flip()
    
    def carregar_arquivos(self):
        #diret=os.path.dirname(__file__)
        direct_imag=os.path.join(os.getcwd(),"imagens")
        self.direct_sons = os.path.join(os.getcwd(),'musics')
        #self.spritesheet = os.path.join(direct_imag)
        self.logo=os.path.join(direct_imag,constantes.logo)
        self.logo=pygame.image.load(self.logo).convert()

    def draw_texto(self,texto,tamanho,cor,x,y):
        fonte=pygame.font.SysFont("inkfree", 25, bold=True, italic=True )  # vai definir a fonte do texto que aparecerá na tela 
        fonte2=pygame.font.SysFont("inkfree", 40, bold=True, italic=True )
        fonte3=pygame.font.SysFont("inkfree", 30, bold=True, italic=True )
        texto=fonte.render(texto,True,cor)
        texto_rect=texto.get_rect()
        texto_rect.midtop=(x,y) #posiciona centro do texto na coordenada x,y
        self.tela.blit(texto,texto_rect)

    def logo_inicio(self,x,y):
        inicio_logo_rect = self.logo.get_rect()
        inicio_logo_rect.midtop = (x,y)
        self.tela.blit(self.logo,inicio_logo_rect)


    def tela_inicio(self):
        self.logo_inicio(constantes.larg/2,20)
        
        self.draw_texto('Pressione uma tecla para jogar',32,constantes.preto,constantes.larg/2,320)
        self.draw_texto('texto blah blah',20,constantes.preto,constantes.larg/2,500)
        pygame.display.flip()
        self.espera_jogador()

    def espera_jogador(self):
        espera=True
        while espera: 
            self.clock.tick(60)
            for event in pygame.events.get():
                if event.type == pygame.QUIT:
                    espera =  False
                    self.rodando = False
                if event.type == pygame.KEYUP:
                    espera = False

    def tela_gameover(self):
        pass

g = Game()
g.tela_inicio()

while g.rodando:
    g.jogo_novo()
    g.tela_gameover()