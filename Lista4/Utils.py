import cv2
import numpy


def mostraImagem(imagem):
    cv2.imshow('imagem', imagem)
    cv2.waitKey(0)
    pass


def leImagem(imagem):
    path = "imagens/"
    return cv2.imread(path + imagem)

def passaFiltroDeMedia(imagem, tamanho):
    return cv2.blur(imagem, (tamanho, tamanho))


def mostraListaDeImagens(list):
    posicao = 0
    for i in range(len(list)):
        cv2.imshow('Imagem ' + str(posicao), list[i])
        posicao += 1
    cv2.waitKey(0)
    pass


def calculaMoedas(moedas):
    soma = 0
    soma += moedas[0] * 25
    soma += moedas[1] * 10
    soma += moedas[2] * 5
    soma += moedas[3]
    print("Valor total = " + str(soma))
    pass