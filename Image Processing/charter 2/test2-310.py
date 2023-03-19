import cv2 as cv
import numpy

def spacedivision(img, a, b, x):
    x = int(256 / x)
    background = numpy.zeros((a, b), dtype=numpy.uint8)
    for i in range(a):
        for j in range(b):
            background[i][j] = int(img[int(i/x)*x][int(j/x)*x])
    return background

img = cv.imread('BioID_0000.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("before256", img)
a = img.shape[0]
b = img.shape[1]
print(a, b)
img = spacedivision(img, a, b, 128)
cv.imshow("after128", img)
img = spacedivision(img, a, b, 64)
cv.imshow("after64", img)
img = spacedivision(img, a, b, 32)
cv.imshow("after32", img)
img = spacedivision(img, a, b, 16)
cv.imshow("after16", img)

cv.waitKey(0)
