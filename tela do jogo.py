import pygame
from random import randint

pygame.init()

x = 525  # posição da seta no eixo x  MIN: 200 MAX: 850
y = 100  # posição da seta no eixo y

pos_lixeira_y = 450  # posição das lixeiras no eixo x - era 300
pos_lixeira_topo = 350

pos_lixeira_papel_x = 250  # posição das lixeiras no eixo y
pos_lixeira_vidro_x = 410
pos_lixeira_organico_x = 570
pos_lixeira_metal_x = 730
pos_lixeira_plastico_x = 890

velocidade = 10  # movimentação da seta em px
lixos = ['caixa papel', 'celular', 'garrafa vidro', 'latinha', 'latinha metal', 'maça', 'plastico', 'sorvete', 'vidro']

# listagem dos tipos de lixo
papel = ['caixa papel']
vidro = ['garrafa vidro', 'vidro']
organico = ['maça', 'sorvete']
metal = ['celular', 'latinha', 'latinha metal']
plastico = ['plastico']

fundo = pygame.image.load('imagens/tela do jogo/fundo.png')  # fundo da tela

l = ''
inicio = 0
fim = 8


def mudarLixo():
    """
    função criada para sortear o lixo da lista
    :return: retorna uma string como o lixo sorteado
    """
    global l
    global inicio
    global fim
    l = randint(inicio, fim)
    lixo = lixos[l]
    return lixo


tipo = 'vazio'

tipo = ''


def definir_tipo(lixo):
    """
    :param lixo: lixo atual que está na tela, sorteado dentro de uma lista
    :return: uma string descrevendo qual o tipo do lixo
    """
    if lixo in papel:
        tipo = 'papel'
    elif lixo in vidro:
        tipo = 'vidro'
    elif lixo in organico:
        tipo = 'organico'
    elif lixo in metal:
        tipo = 'metal'
    elif lixo in plastico:
        tipo = 'plastico'

    return tipo


def mostrarLixoAtual():
    """
    carrega a imagem do lixo na tela
    :return: retorna o carregamento da imagem do lixo
    """
    atual = mudarLixo()  # lixo sorteado dentro da lista
    global tipo  # faz a variavel criada fora da função funcionar dentro da função
    tipo = definir_tipo(atual)
    seta = pygame.image.load('imagens/Lixos/' + atual + '.png')
    return seta


def escolher_lixeira(lixo):
    """
    detecta se o lixo está na lixeira correta,
    o lixo tem que entrar na posição exata de onde está a lixeira,
    o valor 160 define o canto da lixeira
    :param lixo: o lixo que aparece na tela
    :return:
    """
    global y
    global x
    global seta
    global l
    global fim
    lixo_atual = lixos[l]
    if lixo == 'papel' and y > pos_lixeira_topo and pos_lixeira_papel_x - 160 < x < pos_lixeira_papel_x:
        lixos.remove(lixo_atual)
        fim -= 1
        seta = mostrarLixoAtual()
    elif lixo == 'vidro' and y > pos_lixeira_topo and pos_lixeira_vidro_x - 160 < x < pos_lixeira_vidro_x:
        lixos.remove(lixo_atual)
        fim -= 1
        seta = mostrarLixoAtual()
    elif lixo == 'organico' and y > pos_lixeira_topo and pos_lixeira_organico_x - 160 < x < pos_lixeira_organico_x:
        lixos.remove(lixo_atual)
        fim -= 1
        seta = mostrarLixoAtual()
    elif lixo == 'metal' and y > pos_lixeira_topo and pos_lixeira_metal_x - 160 < x < pos_lixeira_metal_x:
        lixos.remove(lixo_atual)
        fim -= 1
        seta = mostrarLixoAtual()
    elif lixo == 'plastico' and y > pos_lixeira_topo and pos_lixeira_plastico_x - 160 < x < pos_lixeira_plastico_x:
        lixos.remove(lixo_atual)
        fim -= 1
        seta = mostrarLixoAtual()
    elif y > pos_lixeira_topo:
        x = 525
        y = 100
    elif len(lixos) == 1:
        fim = pygame.image.load('imagens/tela do jogo/campeao.png')
        janela.blit(fim,(190,45))



seta = mostrarLixoAtual()  # carrega a imagem de um lixo aleatoriamente

# seta = pygame.image.load('imagens/Lixos/latinha.png') exemplo de como está defido o valor do código acima

janela = pygame.display.set_mode((1280, 720))  # tamanho da tela

pausa = pygame.image.load('imagens/tela do jogo/botão pausa.png')  # botão de pause
lazul = pygame.image.load('imagens/tela do jogo/lixo papel.png')  # lixeira azul
lverde = pygame.image.load('imagens/tela do jogo/lixo vidro.png')  # lixeira verde
lmarrom = pygame.image.load('imagens/tela do jogo/lixo organico.png')  # lixeira marrom
lamarela = pygame.image.load('imagens/tela do jogo/lixo metal.png')  # lixeira amarela
lvermelha = pygame.image.load('imagens/tela do jogo/lixo plastico.png')  # lixeira vermelha

pygame.display.set_caption("Hora de reciclar")  # nome que aparece na barra superior da tela
janela_aberta = True
while janela_aberta:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()  # movimentaçao da seta
    if comandos[pygame.K_RIGHT] and x <= 875:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >= 255:
        x -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_UP]:
        y -= velocidade

    janela.blit(fundo, (0, 0))
    janela.blit(seta,(x,y))
    janela.blit(lazul, (pos_lixeira_papel_x, pos_lixeira_y))
    janela.blit(lverde, (pos_lixeira_vidro_x, pos_lixeira_y))
    janela.blit(lmarrom, (pos_lixeira_organico_x, pos_lixeira_y))
    janela.blit(lamarela, (pos_lixeira_metal_x, pos_lixeira_y))
    janela.blit(lvermelha, (pos_lixeira_plastico_x, pos_lixeira_y))




    """
    Quando o lixo encosta em qualquer lixeira ele some
    em desenvolvimento - objetivo é sumir na lixeira correta
    e mudar o lixo

    if (y > pos_lixeira_topo):
        y = 1200
    """

    janela.blit(lazul, (250, pos_lixeira_y))
    janela.blit(lverde, (410, pos_lixeira_y))
    janela.blit(lmarrom, (570, pos_lixeira_y))
    janela.blit(lamarela, (730, pos_lixeira_y))
    janela.blit(lvermelha, (890, pos_lixeira_y))
    pygame.time.delay(7)
    escolher_lixeira(tipo)
    pygame.display.update()

pygame.quit()
