import pygame

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
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            running = False

    tela.fill(branco)
    pygame.draw.circle(tela,preto,(400,300),20)
    pygame.draw.line(tela, preto, (600,300),(400,600),2)

    pygame.display.update()
pygame.quit()