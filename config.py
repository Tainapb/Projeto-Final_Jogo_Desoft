import os


#acessando pasta que contem as sprites 
diret=os.path.dirname(__file__)
direct_imag=os.path.join(diret,"imagens")


#altura do pulo
JUMP_STEP = 15


#definição das cores 
cinza =(127,127,127)
rosa=(200, 0, 100)
preto=(0,0,0)

#definição dos tamanhos 
larg=450
alt=650


score=0  #o score começa em zero 
lives=3  #quantidade de vidas 


rol=0    #rolagem
im_fundo_rol=0  #rolagem da imagem de fundo
rolt_t=200   #velocidade de subida do fundo
max=5#limite de plataformas

pos=100