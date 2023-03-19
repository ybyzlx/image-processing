import matplotlib.pyplot as plt

f_change=[int(0)]*256
for i in range(64):
    f_change[i] = int(i * 0.5)
for i in range(64, 192):
    f_change[i] = int(i * 1.5 - 64)
for i in range(192,256):
    f_change[i] = int(i * 0.5 + 128)

plt.bar(range(256),f_change)
plt.show()

