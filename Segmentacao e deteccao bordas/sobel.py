from matplotlib import pyplot as plt
import cv2
import numpy as np

img = cv2.imread('planeta.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = img[::2, ::2]

imgSuavizada = cv2.GaussianBlur(img, (7,7),0)

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobel = cv2.bitwise_or(sobelX, sobelY)

linha1 = np.hstack([img, sobelX])
linha2 = np.hstack([sobelY, sobel])
res = np.vstack([linha1, linha2])

cv2.imshow("img", res)
cv2.waitKey(0)
