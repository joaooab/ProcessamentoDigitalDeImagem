import Utils

tamanho = 500
imagem = Utils.criaImagem(tamanho,tamanho)

for linha in range(tamanho):
    for coluna in range(tamanho):
        imagem[linha, coluna, 0] = 128
        imagem[linha, coluna, 1] = 255
        imagem[linha, coluna, 2] = 128

Utils.mostraImagem(imagem)
