import cv2
import numpy

import Utils

imagem = Utils.leImagem('grade.png')
imagem = Utils.converteRGBParaHSV(imagem)

H = imagem[:,:,0]

HFiltrado = H
HFiltrado = Utils.passaFiltroDeMedia(HFiltrado, 25)

imagem[:, :, 0] = HFiltrado
imagemResultado = Utils.converteHSVParaRGB(imagem)

cv2.imshow('Original', imagem)
cv2.imshow('H', H)
cv2.imshow('HFiltrado', HFiltrado)
cv2.imshow('imagemResultado', imagemResultado)
cv2.waitKey(0)
