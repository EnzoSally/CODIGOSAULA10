from funcoes import limpartela
import pygame
import time

limpartela()
pygame.init()
tamanho = (800,600)
tela = pygame.display.set_mode( tamanho )
clock = pygame.time.Clock()
running = True
posicaoxbola = 0
branco = (255,255,255)
preto = (0,0,0)

running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif evento.type == pygame.KEYDOWN and evento.key== pygame.K_ESCAPE:
            running = False

    tela.fill(branco)
    pygame.draw.circle(tela, preto, (posicaoxbola,300),54)
    posicaoxbola = posicaoxbola + 1
    
    pygame.display.update()
    clock.tick(60)


pygame.quit()