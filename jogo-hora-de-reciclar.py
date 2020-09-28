import pygame

pygame.init()

fundo = pygame.image.load('tela pura.png') #fundo da tela
logo = pygame.image.load('logo2.png') #logo do jogo
iniciar = pygame.image.load('iniciar.png') #botão iniciar
resultado = pygame.image.load('ver resultado.png') #botão resultado
janela = pygame.display.set_mode((1920,1080)) #tamanho da tela
pygame.display.set_caption("hora de reciclar") # nome que aparece na barra superior da tela

janela_aberta = True
while janela_aberta:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False


    janela.blit(fundo,(0, 0))
    janela.blit(logo,(770,100))
    janela.blit(iniciar,(700,630))
    janela.blit(resultado,(700,730))
    pygame.display.update()

pygame.quit()
