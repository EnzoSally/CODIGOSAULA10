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
    pygame.draw.circle(tela, preto, (68,55),35)
    pygame.draw.line(tela, preto, (68,55),(232,475),1)
    pygame.draw.circle(tela, branco, (68,55),33)

    pygame.draw.circle(tela, preto, (232,475),35)
    pygame.draw.line(tela, preto, (232,475),(432,350),1)
    pygame.draw.circle(tela, branco, (232,475),33)

    pygame.draw.circle(tela, preto, (432,320),35)
    pygame.draw.line(tela, preto, (432,320),(600,320),1)
    pygame.draw.circle(tela, branco, (432,320),33)
    
    pygame.draw.circle(tela, preto, (600,320),35)
    pygame.draw.circle(tela, branco, (600,320),33)

    pygame.display.update()
pygame.quit()