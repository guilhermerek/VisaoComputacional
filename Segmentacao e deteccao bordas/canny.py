from matplotlib import pyplot as plt
import cv2
import numpy as np

img = cv2.imread('planeta.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = img[::2, ::2]

imgSuavizada = cv2.GaussianBlur(img, (7,7),0)

canny1 = cv2.Canny(imgSuavizada, 10, 90)
canny2 = cv2.Canny(imgSuavizada, 50, 200)

linha1 = np.hstack([img, imgSuavizada])
linha2 = np.hstack([canny1, canny2])
res = np.vstack([linha1, linha2])

cv2.imshow("img", res)
cv2.waitKey(0)
