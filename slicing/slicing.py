# Importação das bibliotecas
import cv2
# Leitura da imagem
imagemEntrada = cv2.imread('fotoFullHd.jpg')

#cv2.imread(path, flag)
#Parâmetros:
#path: stw.jpg
#flag: cv2.IMREAD_COLOR #A forma como a imagem deve ser carregada. Por padrão é cv2.IMREAD_COLO
#Retorno: retorna a matriz da imagem carregada


import cv2
import numpy as np
# Leitura da imagem com a função imread()
imagemEntrada = cv2.imread('fotoFullHd.jpg')
#print('Largura (px): ', imagemEntrada.shape[1])
#print('Altura (px): ', imagemEntrada.shape[0])
#print('Quantidade de canais: ', imagemEntrada.shape[2])



#print('B: ', imagemEntrada[100][100][0], 'G: ',
#      imagemEntrada[100][100][1], 'R: ', imagemEntrada[100][100][2])

#for i in range(0, imagemEntrada.shape[1]):
#    for j in range(0, imagemEntrada.shape[0]):
#        if(j > 100 and j < 201):
#            imagemEntrada[j][i][0] = 255
#        if(j > 200 and j < 301):
#            imagemEntrada[j][i][1] = 255
#        if(j > 300 and j < 401):
#            imagemEntrada[j][i][2] = 255
#    
#cv2.imshow("teste", imagemEntrada)

#cv2.waitKey(0)

#cv2.imwrite('nova.jpg', imagemEntrada)


# usando slicing


imagemEntrada = cv2.imread('fotoFullHd.jpg')


imagemEntrada[10:800, 340:1080] = (200, 40, 100)

    


cv2.imwrite('slicing.jpg', imagemEntrada)