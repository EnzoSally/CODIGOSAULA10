from funcoes import limpartela
import pygame

limpartela()
pygame.init()
tamanho = (800,600)
tela = pygame.display.set_mode( tamanho )
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
    pygame.draw.circle(tela, preto, (400,300),79)
    pygame.draw.line(tela, preto, (0,0),(800,600),1)
    pygame.draw.line(tela, preto, (800,0),(0,600),1)
    pygame.draw.circle(tela, branco, (400,300),76)

    pygame.display.update()
pygame.quit()