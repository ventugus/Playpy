import pygame


pygame.init()

fundo = pygame.image.load('imagens/tela inicial/tela-inicial.png') #fundo da tela
logo = pygame.image.load('imagens/tela inicial/logo.png') #logo do jogo
iniciar = pygame.image.load('imagens/tela inicial/iniciar.png') #botão iniciar
resultado = pygame.image.load('imagens/tela inicial/ver resultado.png') #botão resultado
janela = pygame.display.set_mode((1280,720)) #tamanho da tela
pygame.display.set_caption("imagens/tela inicial/hora de reciclar") #nome que aparece na barra superior da tela

janela_aberta = True
while janela_aberta:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False


    janela.blit(fundo,(0, 0))
    janela.blit(logo,(545,100))
    janela.blit(iniciar,(460,410))
    janela.blit(resultado,(460,490))
    pygame.display.update()

pygame.quit()
