import cv2

import Utils

tamanho = 500
imagem = Utils.criaImagem(tamanho,tamanho)

for linha in range(tamanho):
    for coluna in range(tamanho):
        if linha < 250 and coluna > 250:
            imagem[linha, coluna, 0] = 0
            imagem[linha, coluna, 1] = 0
            imagem[linha, coluna, 2] = 255
        elif linha > 250 and coluna < 250:
            imagem[linha, coluna, 0] = 255
            imagem[linha, coluna, 1] = 0
            imagem[linha, coluna, 2] = 0
        else:
            imagem[linha, coluna, 0] = 0
            imagem[linha, coluna, 1] = 255
            imagem[linha, coluna, 2] = 0

Utils.mostraImagem(imagem)
