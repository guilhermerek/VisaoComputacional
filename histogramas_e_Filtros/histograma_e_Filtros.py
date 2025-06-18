from matplotlib import pyplot as plt
import cv2
import numpy as np

img = cv2.imread('fotoFullHd.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

h_eq = cv2.equalizeHist(img)

h_blur = np.vstack([
    np.hstack([img, cv2.blur(img, (3,3))]),
    np.hstack([cv2.blur(img,(5,5)), cv2.blur(img,(11,11))])
])

h_gaussian = np.vstack([
    np.hstack([img, cv2.GaussianBlur(img, (3,3),0)]),
    np.hstack([cv2.GaussianBlur(img,(5,5),0), cv2.GaussianBlur(img,(11,11),0)])
])

h_medianBlur = np.vstack([
    np.hstack([img, cv2.medianBlur(img, 3)]),
    np.hstack([cv2.medianBlur(img,5), cv2.medianBlur(img,11)])
])

#canais = cv2.split(img)
h= cv2.calcHist([img], [0], None, [256], [0,256])

plt.figure()
plt.xlabel("intensidade")
plt.ylabel("QTD Pixels")

plt.plot(h)
plt.xlim([0,256])
plt.show()

plt.hist(img.ravel(), 64, (0,256))
plt.show()

imgSuavizada = cv2.GaussianBlur(img, (7,7),0)
(T, imgBin) = cv2.threshold(
    imgSuavizada,
    100,
    255,
    cv2.THRESH_BINARY
)


bin_invertido = cv2.adaptiveThreshold(imgSuavizada, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                      cv2.THRESH_BINARY_INV, 21, 5)


cv2.imshow("foto",img)
cv2.imshow("foto eq", h_eq)
cv2.imshow("foto blur", h_blur)
cv2.imshow("gaussian", h_gaussian)
cv2.imshow("median", h_medianBlur)

cv2.imshow("img binarizada", imgBin)
cv2.imshow("img bin invertida", bin_invertido)

cv2.waitKey(0)
