from funcoes import limpartela
import pygame
import random
import winsound

limpartela()
pygame.init()
tamanho = (800,600)
tela = pygame.display.set_mode( tamanho )
clock = pygame.time.Clock()
running = True
posicaoxbola = 0
posicaoybola = 0
direita = True
pygame.display.set_caption("SONIC_FLAPPY")
fundo = pygame.image.load("FUNDOSONIC.jpg")
flappy = pygame.image.load("flappy.png")
CANO = pygame.image.load("CANO.png")
flappy_Original = pygame.image.load("flappy.png")
pygame.display.set_icon(flappy)
pygame.mixer.music.load("Trilha.mp3")
pygame.mixer.music.play(-1)
movimentobolaVx = 0
movimentobolaVy = 0
posicaoybolaV = 300
posicaoxbolaV = 400
velocidade = 1
vermelho = (255, 0, 0)
branco = (255,255,255)
preto = (0,0,0)

running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif evento.type == pygame.KEYDOWN and evento.key== pygame.K_ESCAPE:
            running = False
        elif evento.type == pygame.KEYDOWN and evento.key== pygame.K_LEFT:
            movimentobolaVx = -5
            flappy = pygame.transform.flip(flappy,True,False)
        elif evento.type == pygame.KEYDOWN and evento.key== pygame.K_RIGHT:
            movimentobolaVx = 5
            flappy = flappy_Original
        elif evento.type == pygame.KEYUP and evento.key== pygame.K_LEFT:
            movimentobolaVx = 0
        elif evento.type == pygame.KEYUP and evento.key== pygame.K_RIGHT:
            movimentobolaVx = 0
        elif evento.type == pygame.KEYDOWN and evento.key== pygame.K_UP:
            movimentobolaVy = -5
        elif evento.type == pygame.KEYDOWN and evento.key== pygame.K_DOWN:
            movimentobolaVy = 5
        elif evento.type == pygame.KEYUP and evento.key== pygame.K_UP:
            movimentobolaVy = 0
        elif evento.type == pygame.KEYUP and evento.key== pygame.K_DOWN:
            movimentobolaVy = 0


    tela.fill(branco)
    pygame.draw.circle(tela, preto, (posicaoxbola,posicaoybola),54)
    if posicaoxbola >= 800:
        direita = False
       # velocidade = velocidade + 4
        posicaoybola = random.randint(0,600)
       # winsound.Beep(500,300)
    
    elif posicaoxbola <= 0:
        direita = True
        velocidade = velocidade + 4
    
    if direita:
        posicaoxbola = posicaoxbola + velocidade
    
    else:
        posicaoxbola = posicaoxbola - velocidade

    #FAZENDO PAREDES DIREITA E ESQUERDA
    if posicaoxbolaV < 0:
        posicaoxbolaV = 0
    if posicaoxbolaV > 800:
        posicaoxbolaV = 800

    posicaoxbolaV = posicaoxbolaV + movimentobolaVx
    
    #FAZENDO PAREDES CIMA E BAIXO
    if posicaoybolaV < 0:
        posicaoybolaV = 0    
    if posicaoybolaV > 600:
        posicaoybolaV = 600       
    posicaoybolaV = posicaoybolaV + movimentobolaVy
    #pygame.draw.circle(tela,vermelho,(posicaoxbolaV,posicaoybolaV), 30)

    tela.blit(fundo,(0,0))
    tela.blit(flappy,(posicaoxbolaV,posicaoybolaV))
    tela.blit(CANO,(posicaoxbola,posicaoybola))
   


    pygame.display.update()
    clock.tick(60)


pygame.quit()