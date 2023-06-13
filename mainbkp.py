from funcoes import limpartela
import pygame
import random
import winsound

limpartela()
pygame.init()

def gameover():
    tamanho = (800,600)
    tela = pygame.display.set_mode( tamanho )
    clock = pygame.time.Clock()
    running = True
    posicaoxbola = 0
    posicaoybola = 0
    direita = True
    pygame.display.set_caption("SONIC_FLAPPY")
    fundo = pygame.image.load("flappymorto.jpg")
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
    fonte = pygame.font.Font(None,36)
    pontos = 0
    vermelho = (255, 0, 0)
    branco = (255,255,255)
    preto = (0,0,0)

    running = True
    while running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key== pygame.K_ESCAPE:
                quit()
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
            velocidade = velocidade + 1
            pontos = pontos + 1
        # winsound.Beep(500,300)
        
        elif posicaoxbola <= 0:
            direita = True
            pontos = pontos + 1
            velocidade = velocidade + 2
        
        if direita:
            posicaoxbola = posicaoxbola + velocidade
        
        else:
            posicaoxbola = posicaoxbola - velocidade

        #FAZENDO PAREDES DIREITA E ESQUERDA
        if posicaoxbolaV < -40:
            posicaoxbolaV =-40
        if posicaoxbolaV > 750:
            posicaoxbolaV = 750

        posicaoxbolaV = posicaoxbolaV + movimentobolaVx
        
        #FAZENDO PAREDES CIMA E BAIXO
        if posicaoybolaV < -25:
            posicaoybolaV = -25
        if posicaoybolaV > 525:
            posicaoybolaV = 525       
        posicaoybolaV = posicaoybolaV + movimentobolaVy
        #pygame.draw.circle(tela,vermelho,(posicaoxbolaV,posicaoybolaV), 30)

        tela.blit(fundo,(0,0))
        tela.blit(flappy,(posicaoxbolaV,posicaoybolaV))
        tela.blit(CANO,(posicaoxbola,posicaoybola))
    
        pixelXFlappy = list(range(posicaoxbolaV,posicaoxbolaV + 100)) #+os pixels dele
        pixelyFlappy = list(range(posicaoybolaV,posicaoybolaV + 54))
        pixelXcano = list(range(posicaoxbola, posicaoxbola + 100))
        pixelycano = list(range(posicaoybola, posicaoybola + 144))

        totalpixelaltura = len(list(set(pixelXFlappy)& set(pixelXcano))) #testar os pixels
        totalpixellargura = len(list(set(pixelyFlappy)& set(pixelycano))) #testar os pixels

        if totalpixelaltura > 12:
            if totalpixellargura > 28:
                running = False
                jogo()

        texto = fonte.render("SCORE:"+str(pontos), True, preto)
        tela.blit(texto,(50,30))

def jogo():

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
    fonte = pygame.font.Font(None,36)
    pontos = 0
    vermelho = (255, 0, 0)
    branco = (255,255,255)
    preto = (0,0,0)

    running = True
    while running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key== pygame.K_ESCAPE:
                quit()
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
            velocidade = velocidade + 1
            pontos = pontos + 1
        # winsound.Beep(500,300)
        
        elif posicaoxbola <= 0:
            direita = True
            pontos = pontos + 1
            velocidade = velocidade + 2
        
        if direita:
            posicaoxbola = posicaoxbola + velocidade
        
        else:
            posicaoxbola = posicaoxbola - velocidade

        #FAZENDO PAREDES DIREITA E ESQUERDA
        if posicaoxbolaV < -40:
            posicaoxbolaV =-40
        if posicaoxbolaV > 750:
            posicaoxbolaV = 750

        posicaoxbolaV = posicaoxbolaV + movimentobolaVx
        
        #FAZENDO PAREDES CIMA E BAIXO
        if posicaoybolaV < -25:
            posicaoybolaV = -25
        if posicaoybolaV > 525:
            posicaoybolaV = 525       
        posicaoybolaV = posicaoybolaV + movimentobolaVy
        #pygame.draw.circle(tela,vermelho,(posicaoxbolaV,posicaoybolaV), 30)

        tela.blit(fundo,(0,0))
        tela.blit(flappy,(posicaoxbolaV,posicaoybolaV))
        tela.blit(CANO,(posicaoxbola,posicaoybola))
    
        pixelXFlappy = list(range(posicaoxbolaV,posicaoxbolaV + 100)) #+os pixels dele
        pixelyFlappy = list(range(posicaoybolaV,posicaoybolaV + 54))
        pixelXcano = list(range(posicaoxbola, posicaoxbola + 100))
        pixelycano = list(range(posicaoybola, posicaoybola + 144))

        totalpixelaltura = len(list(set(pixelXFlappy)& set(pixelXcano))) #testar os pixels
        totalpixellargura = len(list(set(pixelyFlappy)& set(pixelycano))) #testar os pixels

        if totalpixelaltura > 12:
            if totalpixellargura > 28:
                running = False
                jogo()

        texto = fonte.render("SCORE:"+str(pontos), True, preto)
        tela.blit(texto,(50,30))

        pygame.display.update()
        clock.tick(60)
jogo()

pygame.quit()