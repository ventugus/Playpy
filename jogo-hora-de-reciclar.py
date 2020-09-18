import pygame

pygame.init()

janela = pygame.display.set_mode((1920,1080)) #tamanho da tela
pygame.display.set_caption("hora de reciclar") # nome que aparece na barra superior da tela

janela_aberta = True
while janela_aberta:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

pygame.quit()