import cv2
import numpy as np

imagemEntrada = cv2.imread('fotoFullHd.jpg')
linha, coluna, _ = imagemEntrada.shape
m = np.float32([
    [1, 0 , 50],
    [0, 1, 90]
])

saida = cv2.warpAffine(imagemEntrada, m, (coluna, linha))
cv2.imshow('saida', saida)
cv2.waitKey(0)
cv2.destroyAllWindows()

#rotacao de imagem

centro = (coluna // 2, linha // 2)
m2 = cv2.getRotationMatrix2D(centro, 25, 1.0)
saida2 = cv2.warpAffine(imagemEntrada, m2, (coluna, linha))
cv2.imshow('saida2', saida2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#mascara

radius = min(coluna,linha // 4)
mascara = np.zeros(imagemEntrada.shape[:2], dtype='uint8')
cv2.circle(mascara, centro, radius, (255), -1)
imgMascara = cv2.bitwise_and(src1=imagemEntrada, src2=imagemEntrada, mask=mascara)
cv2.imshow('imgmascara', imgMascara)
cv2.waitKey(0)
cv2.destroyAllWindows()

