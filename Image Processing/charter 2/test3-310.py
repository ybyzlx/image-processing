import cv2 as cv
import numpy as np

def adivision(img, a, b, x):
    x = int(256 / x)
    background = np.zeros((a, b), dtype=np.uint8)
    for i in range(a):
        for j in range(b):
            background[i][j] = (int(img[i][j] / x)+1) * x -1
    return background


img = cv.imread('BioID_0000.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("before256", img)
a = img.shape[0]
b = img.shape[1]
img = adivision(img, a, b, 128)
cv.imshow("after128", img)
img = adivision(img, a, b, 64)
cv.imshow("after64", img)
img = adivision(img, a, b, 32)
cv.imshow("after32", img)
img = adivision(img, a, b, 16)
cv.imshow("after16", img)
img = adivision(img, a, b, 8)
cv.imshow("after8", img)
img = adivision(img, a, b, 4)
cv.imshow("after4", img)
img = adivision(img, a, b, 2)
cv.imshow("after2", img)
cv.waitKey(0)
