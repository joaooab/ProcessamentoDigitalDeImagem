import cv2
import numpy


def criaImagem(linhas, colunas):
    imagem = numpy.ones((linhas, colunas), numpy.uint8)
    imagem = cv2.cvtColor(imagem, cv2.COLOR_GRAY2BGR)
    return imagem


def mostraImagem(imagem):
    cv2.imshow('imagem', imagem)
    cv2.waitKey(0)
    pass


def leImagem(imagem):
    path = "imagens/"
    return cv2.imread(path + imagem)


def getMonocromatico(blue, gree, red):
    monocromatico = (int(blue) + int(gree) + int(red)) / 3
    return monocromatico


def converteRGBParaHSV(imagem):
    return cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV_FULL)


def converteHSVParaRGB(imagem):
    return cv2.cvtColor(imagem, cv2.COLOR_HSV2BGR_FULL)


def passaFiltroDeMedia(imagem, tamanho):
    return cv2.blur(imagem, (tamanho, tamanho))


def mostraListaDeImagens(list):
    posicao = 0
    for i in range(len(list)):
        cv2.imshow('Imagem ' + str(posicao), list[i])
        posicao += 1
    cv2.waitKey(0)
    pass