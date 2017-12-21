import cv2
import numpy

import Utils

imagemOriginal = Utils.leImagem("frango.tif")
imagemRuidosa = cv2.cvtColor(imagemOriginal, cv2.COLOR_RGB2GRAY)

dimensoes = numpy.shape(imagemRuidosa)
linhas = dimensoes[0]
colunas = dimensoes[1]

for linha in range(linhas):
    for coluna in range(colunas):
        pixel = imagemRuidosa[linha, coluna]
        if (pixel >= 0 and pixel <= 200):
            imagemRuidosa[linha, coluna] = 0

kernel = numpy.ones((5, 5), numpy.uint8)
imagemErosao = cv2.erode(imagemRuidosa, kernel)
imageResultado, contours, hierarchy = cv2.findContours(imagemErosao, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print("Contador: " + str(len(contours)))

lista = []
lista.append(imagemOriginal)
lista.append(imagemRuidosa)
lista.append(imageResultado)
Utils.mostraListaDeImagens(lista)
