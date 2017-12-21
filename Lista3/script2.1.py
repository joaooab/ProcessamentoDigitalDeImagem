import cv2
import numpy

import Utils

imagem = Utils.leImagem('fig_lista4_1.bmp')

dimensoes = numpy.shape(imagem)
linhas = dimensoes[0]
colunas = dimensoes[1]
dimensoes = dimensoes[2]

coresSeguras = [0, 51, 102, 153, 204, 255]


def trocaParaCorSegura(dimensao):
    pixel = imagem[linha, coluna, dimensao]
    if pixel >= 0 and pixel <= 43:
        pixel = coresSeguras[0]
    elif pixel >= 44 and pixel <= 86:
        pixel = coresSeguras[1]
    elif pixel >= 87 and pixel <= 129:
        pixel = coresSeguras[2]
    elif pixel >= 130 and pixel <= 172:
        pixel = coresSeguras[3]
    elif pixel >= 173 and pixel <= 215:
        pixel = coresSeguras[4]
    elif pixel >= 216 and pixel <= 255:
        pixel = coresSeguras[5]
    return pixel


for linha in range(linhas):
    for coluna in range(colunas):
        imagem[linha, coluna, 0] = trocaParaCorSegura(0)
        imagem[linha, coluna, 1] = trocaParaCorSegura(1)
        imagem[linha, coluna, 2] = trocaParaCorSegura(2)

Utils.mostraImagem(imagem)

# imagem = Utils.mostraImagem(imagem)
