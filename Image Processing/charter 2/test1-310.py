# 同时对比度
import cv2
import numpy


def black(img, x):
    a = img.shape[0]
    for j in range(a):
        img[j] = x
    return img

w = 200
s = 20
back = numpy.zeros((w, w), dtype=numpy.uint8)
back = black(back, 64)
for i in range(int(w / 2 - s), int(w / 2 + s)):
    for j in range(int(w / 2 - s), int(w / 2 + s)):
        back[i][j] = 128
cv2.imshow('test1', back)
back = black(back, 192)
for i in range(int(w / 2 - s), int(w / 2 + s)):
    for j in range(int(w / 2 - s), int(w / 2 + s)):
        back[i][j] = 128
cv2.imshow('test2', back)

cv2.waitKey(0)
