import cv2
import numpy as np

imagemEntrada = cv2.imread('fotoFullHd.jpg')
linha, coluna, _ = imagemEntrada.shape

#Aplicar um roação de 45 graus sobre ela e salvar como imagem rotacionada;

centro = (coluna // 2, linha // 2)
m2 = cv2.getRotationMatrix2D(centro, 55, 1.0)
saida2 = cv2.warpAffine(imagemEntrada, m2, (coluna, linha))
cv2.imshow('saida2', saida2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#aplicar uma ransformação de redimensionameno para ampliar a imagem em 30% e salvar a nova imagem;

altura = imagemEntrada.shape[0]
largura = imagemEntrada.shape[1]

largura_nova = int(largura * 1.3)
altura_nova = int(altura * 1.3)
tamanho_novo = (largura_nova, altura_nova)

nova_imagem = cv2.resize(src=imagemEntrada,dsize=tamanho_novo, interpolation=cv2.INTER_LANCZOS4)
print(nova_imagem.shape)
cv2.imwrite('redimensionar.jpg', nova_imagem)
cv2.imshow('saida2', nova_imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()


#aplicar uma máscara usando um retângulo e gerar uma nova imagem.


radius = min(coluna,linha // 4)
mascara = np.zeros(imagemEntrada.shape[:2], dtype='uint8')
cv2.rectangle(mascara, (600,800) , centro, (255), -1)
imgMascara = cv2.bitwise_and(src1=imagemEntrada, src2=imagemEntrada, mask=mascara)
cv2.imshow('imgmascara', imgMascara)
cv2.waitKey(0)
cv2.destroyAllWindows()

