import Utils

imagem = Utils.leImagem("cores.tif")

B = imagem[:,:,0]
G = imagem[:,:,1]
R = imagem[:,:,2]

lista = []
lista.append(B)
lista.append(G)
lista.append(R)
Utils.mostraListaDeImagens(lista)

