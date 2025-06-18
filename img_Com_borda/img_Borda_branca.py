# Guilherme Rek Castanha
#12. Crie um algoritmo em Python que abra uma dada imagem, crie uma borda de
# 50 pixels ao entorno da imagem (como se fosse uma moldura de um quadro). Salve
# essa imagem com o nome: imagemEmoldurada.jpg. Entregue o código, a imagem original e
# a imagem ajustada.

import cv2
import numpy as np

imagem = cv2.imread('img_guilherme.jpg')
linha, coluna, canal = imagem.shape

for l in range(linha):
    for c in range(coluna):
        if(l>=0 and l<=50):
            imagem[l][c][0]=255
            imagem[l][c][1]=255
            imagem[l][c][2]=255
        if (c>=1870 and c<=1920):
            imagem[l][c][0]=255
            imagem[l][c][1]=255
            imagem[l][c][2]=255
        if (c>=0 and c<=50):
            imagem[l][c][0]=255
            imagem[l][c][1]=255
            imagem[l][c][2]=255
        if (l>=1030 and l<=1080):
            imagem[l][c][0]=255
            imagem[l][c][1]=255
            imagem[l][c][2]=255


cv2.imwrite('imagemEmoldurada.jpg', imagem)
