import pygame
from random import randint

pygame.init()

x = 525 # posição da seta no eixo x  MIN: 200 MAX: 850
y = 100 # posição da seta no eixo y

pos_lixeira_y = 300 # posição das lixeiras no eixo x
pos_lixeira_topo = 200

pos_lazul_x = 250 # posição das lixeiras no eixo y
pos_lverde_x = 410
pos_lmarrom_x = 570
pos_lamarela_x = 730
pos_lvermelha_x = 890

velocidade = 10 # movimentação da seta em px


lixos = ['caixa papel', 'celular', 'garrafa vidro', 'latinha', 'latinha metal', 'maça', 'plastico', 'sorvete', 'vidro']

fundo = pygame.image.load('imagens/tela do jogo/fundo.png') #fundo da tela


def mudarLixo():
    """
    função criada para sortear o lixo da lista
    :return: retorna uma string como o lixo sorteado
    """
    l = randint(0, 8)
    lixo = lixos[l]
    return lixo

def mostrarLixoAtual():
    """
    carrega a imagem do lixo na tela
    :return: retorna o carregamento da imagem do lixo
    """
    seta = pygame.image.load('imagens/Lixos/' + mudarLixo() + '.png')
    return seta

seta = mostrarLixoAtual() # carrega a imagem de um lixo aleatoriamente

#seta = pygame.image.load('imagens/Lixos/latinha.png')

janela = pygame.display.set_mode((1280,720)) #tamanho da tela
pontuacao = pygame.image.load('imagens/tela do jogo/pontuação.png') #pontuação do jogo
tempo = pygame.image.load('imagens/tela do jogo/tempo.png') #tempo do jogo
som = pygame.image.load('imagens/tela do jogo/botão com som.png') #botão de som
pausa = pygame.image.load('imagens/tela do jogo/botão pausa.png') # botão de pause
lazul = pygame.image.load('imagens/tela do jogo/lixeira azul.png') #lixeira azul
lverde = pygame.image.load('imagens/tela do jogo/lixeira verde.png') #lixeira verde
lmarrom = pygame.image.load('imagens/tela do jogo/lixeira marrom.png') #lixeira marrom
lamarela = pygame.image.load('imagens/tela do jogo/lixeira amarela.png') #lixeira amarela
lvermelha = pygame.image.load('imagens/tela do jogo/lixeira vermelha.png') #lixeira vermelha
pygame.display.set_caption("imagens/hora de reciclar") # nome que aparece na barra superior da tela

janela_aberta = True
while janela_aberta:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed() #movimentaçao da seta
    if comandos[pygame.K_RIGHT] and x<= 850:
        x += velocidade
    if comandos[pygame.K_LEFT] and x>= 200:
        x -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_UP]:
        y -= velocidade


    janela.blit(fundo,(0, 0))
    janela.blit(pontuacao,(450,20))
    janela.blit(tempo,(600,20))
    janela.blit(som,(1100,20))
    janela.blit(pausa,(1170,20))
    janela.blit(seta, (x, y))
    janela.blit(lazul, (pos_lazul_x, pos_lixeira_y))
    janela.blit(lverde, (pos_lverde_x, pos_lixeira_y))
    janela.blit(lmarrom, (pos_lmarrom_x, pos_lixeira_y))
    janela.blit(lamarela, (pos_lamarela_x, pos_lixeira_y))
    janela.blit(lvermelha, (pos_lvermelha_x, pos_lixeira_y))

    if (y > pos_lixeira_topo):
        y = 1200

    pygame.display.update()


pygame.quit()
