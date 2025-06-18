#Guilherme Rek Castanha

# Com base nos conceitos e fundamentos estudados sobre segmentação e detecção de bordas
# desenvolva um programa capaz de abrir uma imagem em alta definição (HD) contendo múltiplos
# edifícios.

import cv2
import numpy as np
img = cv2.imread('edificios.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#    1. Pré-processamento: aplicar uma técnica de suavização (como o filtro Gaussiano)
# para reduzir ruídos e facilitar a detecção de bordas;

imgSuavizada = cv2.GaussianBlur(img, (17,17),0)

#    2. Detecção com Sobel: aplicar o operador de Sobel para detecção
# de bordas e salvar a imagem resultante;

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobel = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow("img", sobel)
cv2.waitKey(0)
cv2.imwrite('sobel.jpg', sobel)

#   3. Detecção com Canny: aplicar o algoritmo de Canny e salvar a respectiva imagem resultante.

canny = cv2.Canny(imgSuavizada, 40, 60)
cv2.imshow("img2", canny)
cv2.waitKey(0)
cv2.imwrite('canny.jpg', canny)

#Sobel
    # É uma tecnica classica, pertencendo a familia de filtros derivativos, que são
    # projetados para realçar bordas
    # estima onde há variação luminosa de cada pixel e aponta onde há variações significativas.

#Canny
    # O Canny é um algorimo de detecção de bordas muito influente e robusto
    # Combina multiplas etapas para tentar identificar melhor as bordas verdadeiras e evitar erros
    # busca cumprir 3 criterios, baixa taxa de erro, boa localização e resposta unica.
    # desta forma, bordas reais devem ser detectadas e os ruidos eliminados
    # a borda que é detectada deve ser o mais proximo da borda real da imagem
    # apenas uma resposta por borda