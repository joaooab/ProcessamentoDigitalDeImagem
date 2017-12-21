import cv2
import numpy

import Utils

#Como a biblioteca opencv não tem função para converter para HSI, a conversão foi feita no matalab
#http://www.mathworks.com/matlabcentral/fileexchange/13630-rgb-to-hsi-conversion?focused=5084558&tab=function
imagem = Utils.leImagem("coresHSI.tif")

H = imagem[:,:,0]
S = imagem[:,:,1]
I = imagem[:,:,2]

lista = []
lista.append(H)
lista.append(S)
lista.append(I)
Utils.mostraListaDeImagens(lista)