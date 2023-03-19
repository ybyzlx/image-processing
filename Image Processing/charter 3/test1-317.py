import cv2
import matplotlib.pyplot as plt
#生成灰度直方图

def gray_plots(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    a = img.shape[0]
    b = img.shape[1]
    sta = [int(0)] * 256
    for i in range(a):
        for j in range(b):
            temp = int(img[i][j])
            sta[temp] = sta[temp] + 1
    return sta

pa = 'BioID_0000.jpg'
plt.bar(range(256), gray_plots(pa))
plt.show()
