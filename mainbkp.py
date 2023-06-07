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
        elif evento.type == pygame.KEYDOWN and evento.key== pygame.K_RIGHT:
            movimentobolaVx = 5
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
    # pygame.draw.circle(tela, preto, (posicaoxbola,posicaoybola),54)
    if posicaoxbola >= 800:
        direita = False
        velocidade = velocidade + 4
        posicaoybola = random.randint(0,600)
        winsound.Beep(500,300)
    
    elif posicaoxbola <= 0:
        direita = True
        velocidade = velocidade + 4
    
    if direita:
        posicaoxbola = posicaoxbola + velocidade
    
    else:
        posicaoxbola = posicaoxbola - velocidade


    if posicaoybolaV >= 800:
        direita = False

    posicaoxbolaV = posicaoxbolaV + movimentobolaVx
    posicaoybolaV = posicaoybolaV + movimentobolaVy
    pygame.draw.circle(tela,vermelho,(posicaoxbolaV,posicaoybolaV), 30)


    pygame.display.update()
    clock.tick(60)


pygame.quit()