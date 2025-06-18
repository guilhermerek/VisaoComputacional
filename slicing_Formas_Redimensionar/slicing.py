import cv2

vermelho = (0,0,255)
verde = (0,255,0)
azul = (255,0,0)


imagemEntrada = cv2.imread('fotoFullHd.jpg')
imagemEntrada[10:800, 340:1080] = (200, 40, 100)

cv2.imwrite('slicing.jpg', imagemEntrada)

imagem2 = cv2.imread('fotoFullHd.jpg')
cv2.line(imagem2, (10,50), (300,50), vermelho, 6)
cv2.rectangle(imagem2, (600,800), (1500,900), verde, 9)
cv2.circle(imagem2, (1000,300), 100, azul,30)

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(imagem2, 'Star Wars', (10, 40), font, 1, (222, 255, 255), 2, cv2.LINE_AA)

cv2.imwrite('formas.jpg', imagem2)


imagem3 = cv2.imread('fotoFullHd.jpg')
recorte = imagem3[240:1600, 360:1000]
cv2.imwrite('recorte.jpg', recorte)


imagem4 = cv2.imread('fotoFullHd.jpg')

altura = imagem4.shape[0]
largura = imagem4.shape[1]

proporcao = float(largura/altura)
largura_nova = 320
altura_nova = int(largura_nova*proporcao)
tamanho_novo = (largura_nova, altura_nova)

nova_imagem = cv2.resize(src=imagem4,dsize=tamanho_novo, interpolation=cv2.INTER_LANCZOS4)
print(nova_imagem.shape)
cv2.imwrite('redimensionar.jpg', nova_imagem)



imagem5 = cv2.imread('fotoFullHd.jpg')

altura = imagem5.shape[0]
largura = imagem5.shape[1]

flip_v = cv2.flip(imagem5, 0)
cv2.imshow('vertical', flip_v)

flip_h = cv2.flip(imagem5, 1)
cv2.imshow('horizontal', flip_h)

flip_hv = cv2.flip(imagem5, -1)
cv2.imshow('hv', flip_hv)

cv2.waitKey(0)
cv2.destroyAllWindows()

