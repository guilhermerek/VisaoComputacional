
#aatividade A
import cv2
imagemEntrada = cv2.imread('foto.jpg')
print('Largura (px): ', imagemEntrada.shape[1])
print('Altura (px): ', imagemEntrada.shape[0])
print('Quantidade de canais: ', imagemEntrada.shape[2])



print('B: ', imagemEntrada[100][100][0], 'G: ', imagemEntrada[100][100][1], 'R: ', imagemEntrada[100][100][2])

#atividade b

for i in range(0, imagemEntrada.shape[1]):
    for j in range(0, imagemEntrada.shape[0]):
        imagemEntrada[j][i][2] = 10

    
cv2.imshow("teste", imagemEntrada)

cv2.waitKey(0)

cv2.imwrite('atividadeB.jpg', imagemEntrada)


#ativividade C
imagemEntrada2 = cv2.imread('foto.jpg')

for i in range(0, imagemEntrada2.shape[1]):
    for j in range(0, imagemEntrada2.shape[0]):
        if(j >0  and j < 50):
            imagemEntrada2[j][i][0] = 255
            imagemEntrada2[j][i][1] = 255
            imagemEntrada2[j][i][2] = 255

cv2.imshow("teste", imagemEntrada2)

cv2.waitKey(0)

cv2.imwrite('atividadeC.jpg', imagemEntrada2)