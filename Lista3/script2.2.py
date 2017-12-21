import numpy
import Utils

c1 = input("Primeiro nível de cinza: ")
c2 = input("Segundo nível de cinza: ")

imagem = Utils.leImagem("fig_lista4_2.bmp")
dimensoes = numpy.shape(imagem)

linhas = dimensoes[0]
colunas = dimensoes[1]
dimensoes = dimensoes[2]

for dimensao in range(dimensoes):
    for linha in range(linhas):
        for coluna in range(colunas):
            pixel = imagem[linha, coluna, dimensao]
            if pixel >= int(c1) and pixel <= int(c2):
                if (dimensao != 0):
                    imagem[linha, coluna, dimensao] = 255
                else:
                    imagem[linha, coluna, dimensao] = 0

Utils.mostraImagem(imagem)
