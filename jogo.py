import os
import sys
import pygame
from pygame.locals import*
import random
import time

from config import*
from classes import*


pygame.init()
pygame.mixer.init()

tela_de_inicio()
game=True
vai =True
while game:
    clock.tick(60) #o jogo não vai rodar mais rapido que 60 FPS por segundo 
    eventos=pygame.event.get() #retorna uma lista com os comandos que o usuário fez no teclado 
    if vai ==True: 
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
            if score>150: 
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
            tela_over()
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
            imagem_fundo=pygame.transform.scale(imagem_fundo, (larg, alt))
            game_over=False

        #todas.draw(tela)

    pygame.display.update()