import cv2 as cv
import matplotlib.pyplot as plt

# 灰度增强变换

def liner_gray(a,b,img):
    for i in range(a):
        for j in range(b):
            r = int(img[i][j])
            if r in range(128):
                img[i][j] = 0
            else:
                img[i][j] = 255
    return img
def gray_plot(img, a, b):
    sta = [int(0)]*256
    for i in range(a):
        for j in range(b):
            temp = int(img[i][j])
            sta[temp] = sta[temp] + int(1)
    return sta

img = cv.imread('BioID_0000.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
a = img.shape[0]
b = img.shape[1]
cv.imshow("before",img)
plt.bar(range(256), gray_plot(img, a, b))
plt.show()
img = liner_gray(a,b,img)
cv.imshow("after",img)
plt.bar(range(256), gray_plot(img, a, b))
plt.show()
