import cv2

imagem = cv2.imread('foto.jpg')
cv2.imwrite('novaExtensao.tiff', imagem)