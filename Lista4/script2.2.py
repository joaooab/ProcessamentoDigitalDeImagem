import cv2
import numpy

import Utils

imagemOriginal = Utils.leImagem("coins1.png")
imagemCinza = cv2.cvtColor(imagemOriginal, cv2.COLOR_RGB2GRAY)
ret, imagemBinaria = cv2.threshold(imagemCinza, 170, 255, cv2.THRESH_BINARY_INV)

kernelDilatacao = numpy.ones((5, 5), numpy.uint8)
imagemComDilatacao = cv2.dilate(imagemBinaria, kernelDilatacao)

kernelErosao = numpy.ones((10, 10), numpy.uint8)
imagemComErocao = cv2.erode(imagemComDilatacao, kernelErosao)

imagemResultado = cv2.medianBlur(imagemComErocao, 5)
imagemResultado, contours, hierarchy = cv2.findContours(imagemResultado, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cents25 = 0
cents10 = 0
cents5 = 0
cents1 = 0
for i in range(8):
    tamanho = len(contours[i])
    if (tamanho >= 195 and tamanho <= 210):
        cents25 += 1
    elif (int(tamanho) >= 170 and int(tamanho) <= 180):
        cents10 += 1
    elif (int(tamanho) >= 150 and int(tamanho) <= 160):
        cents1 += 1
    elif (int(tamanho) >= 140 and int(tamanho) <= 149):
        cents5 += 1
    else:
        print("Tamanho de moeda nao definido")

print("25 cents = " + str(cents25))
print("10 cents = " + str(cents10))
print("5 cents = " + str(cents5))
print("1 cents = " + str(cents1))

moedas = [cents25, cents10, cents5, cents1]
Utils.calculaMoedas(moedas)

lista = []
lista.append(imagemOriginal)
lista.append(imagemCinza)
lista.append(imagemBinaria)
lista.append(imagemComDilatacao)
lista.append(imagemComErocao)
lista.append(imagemResultado)
Utils.mostraListaDeImagens(lista)