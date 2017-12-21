import cv2
import numpy

import Utils

imagem = Utils.leImagem('grade.png')
imagem = Utils.converteRGBParaHSV(imagem)

S = imagem[:, :, 1]

HFiltrado = S
HFiltrado = Utils.passaFiltroDeMedia(HFiltrado, 25)

imagem[:, :, 1] = HFiltrado
imagemResultado = Utils.converteHSVParaRGB(imagem)

list = []
list.append(imagem)
list.append(S)
list.append(HFiltrado)
list.append(imagemResultado)
Utils.mostraListaDeImagens(list)