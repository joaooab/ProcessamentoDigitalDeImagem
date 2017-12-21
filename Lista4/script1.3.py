import cv2

import Utils

imagemOrignal = Utils.leImagem("utk.tif")
elementoEstruturante = Utils.leImagem("eleEs.tif")

imagemOrignal = cv2.cvtColor(imagemOrignal, cv2.COLOR_RGB2GRAY)
elementoEstruturante = cv2.cvtColor(elementoEstruturante, cv2.COLOR_RGB2GRAY)

ret, A = cv2.threshold(imagemOrignal, 170, 255, cv2.THRESH_BINARY)
ret2, D = cv2.threshold(elementoEstruturante, 170, 255, cv2.THRESH_BINARY)

imagemComErocao = cv2.erode(A, D)

ret, Ac = cv2.threshold(imagemOrignal, 170, 255, cv2.THRESH_BINARY_INV)
ret, Dc = cv2.threshold(elementoEstruturante, 170, 255, cv2.THRESH_BINARY_INV)

imagemComErocao2 = cv2.erode(Ac,Dc)

imagemFinal = cv2.bitwise_and(imagemComErocao,imagemComErocao2)

lista = []
lista.append(imagemOrignal)
lista.append(elementoEstruturante)
lista.append(imagemComErocao)
lista.append(imagemComErocao2)
lista.append(Ac)
lista.append(Dc)
lista.append(imagemFinal)
Utils.mostraListaDeImagens(lista)