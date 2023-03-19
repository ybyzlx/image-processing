import cv2
import matplotlib.pyplot as plt
import math as m


# 对一组数据求其直方图
# 对该组数据进行一定的变换求其直方图
# 对该组数据进行均衡化处理

def change_f(r):
    r = int(r)
    return int(m.sqrt(7 * r) + 0.5)

#获取量化后对应的灰度
def balance_f(r, r_array):
    add_sum = 0
    r = int(r)
    for i in range(r):
        add_sum += r_array[i]
    return round(add_sum * 7.0)


r1 = 0.19 * 100
r2 = 0.25 * 100
r3 = 0.21 * 100
r4 = 0.16 * 100
r5 = 0.08 * 100
r6 = 0.06 * 100
r7 = 0.03 * 100
r8 = 0.02 * 100

r_array = [0.19, 0.25, 0.21, 0.16, 0.08, 0.06, 0.03, 0.02]

sta = [int(0)] * 8
sta[0] = int(r1)
sta[1] = int(r2)
sta[2] = int(r3)
sta[3] = int(r4)
sta[4] = int(r5)
sta[5] = int(r6)
sta[6] = int(r7)
sta[7] = int(r8)

plt.bar(range(8), sta)
plt.show()

# sta[0]=change_f(r1)
# sta[1]=change_f(r2)
# sta[2]=change_f(r3)
# sta[3]=change_f(r4)
# sta[4]=change_f(r5)
# sta[5]=change_f(r6)
# sta[6]=change_f(r7)
# sta[7]=change_f(r8)
#
# plt.bar(range(8), sta)
#
# plt.show()

sta1 = [int(0)] * 8
sta2 = [int(0)] * 8

#获取序列
for i in range(1, 9):
    sta1[i - 1] = balance_f(i, r_array)

#合并
n = 0
for j in sta1:
    sta2[j] += sta[n]
    n += 1

plt.bar(range(8), sta2)
plt.show()
