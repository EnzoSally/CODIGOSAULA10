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
    pygame.draw.line(tela, preto, (0,300),(800,300),1)
    pygame.draw.line(tela, preto, (100,120),(100,500),1)
    pygame.draw.line(tela, preto, (100,120),(175,350),1)
    pygame.draw.line(tela, preto, (175,350),(225,189),1)
    pygame.draw.line(tela, preto, (225,189),(225,450),1)
    pygame.draw.line(tela, preto, (225,450),(450,100),1)
    pygame.draw.line(tela, preto, (450,100),(732,450),1)

    pygame.display.update()
pygame.quit()