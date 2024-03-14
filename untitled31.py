# -*- coding: utf-8 -*-
"""Untitled31.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lB-7l82QUKCog10rvUggIqqONS88ToB4
"""

#kurva parabolik
import matplotlib.pyplot as plt
import numpy as np

#Tentukan wilayah (domain) diagram Cartesian dan rasio lebar dan tinggi diagram
x = np.linspace(-4,4,10000)
plt.figure(figsize=(3,30))


#Gambar lingkarang kecil (titik) pada (0,0)
plt.plot(x, (0.01-x**2)**0.5, '-k')
plt.plot(x, -((0.01-x**2)**0.5), '-k')

#Tentukan persamaan matematika yang diinginkan
y = x - x - 0
y1 = x**3 - 2*x**2 - 5*x +6

plt.plot(x, y, '-k')

plt.plot(x, y1, '-r', label='y1')

plt.legend(loc='upper left')
plt.grid()
plt.show()

#latihan kurva
import matplotlib.pyplot as plt
import numpy as np

#Tentukan wilayah (domain) diagram Cartesian dan rasio lebar dan tinggi diagram
x = np.linspace(-3,3,10000)
plt.figure(figsize=(3,30))


#Gambar lingkarang kecil (titik) pada (0,0)
plt.plot(x, (0.01-x**2)**0.5, '-k')
plt.plot(x, -((0.01-x**2)**0.5), '-k')

#Tentukan persamaan matematika yang diinginkan
y = x - x - 0
y1 = -(x**3 - 2*x**2 - x +2)

plt.plot(x, y, '-k')

plt.plot(x, y1, '-r', label='y1')

plt.legend(loc='upper left')
plt.grid()
plt.show()

#lingkaran
import matplotlib.pyplot as plt
import numpy as np

#Tentukan wilayah (domain) diagram Cartesian dan rasio lebar dan tinggi diagram
x = np.linspace(-8,8,10000)
plt.figure(figsize=(8,6.5))

#Tentukan persamaan matematika yang diinginkan
y = x -x -0
y1 = (4-x**2)**0.5
y2 = -(4-x**2)**0.5

y3 = 5 + (4-(x-5)**2)**0.5
y4 = 5 - (4-(x-5)**2)**0.5

y5 = -5 + (4-(x-5)**2)**0.5
y6 = -5 - (4-(x-5)**2)**0.5

y7 = 5 + (4-(x+5)**2)**0.5
y8 = 5 - (4-(x+5)**2)**0.5

y9 = -5 + (4-(x+5)**2)**0.5
y10 = -5 - (4-(x+5)**2)**0.5

plt.plot(x, y, '-k')
plt.plot(x, y1, '-r', label='y1, y2')
plt.plot(x, y2, '-r')
plt.plot(x, y3, '-g', label='y3, y4')
plt.plot(x, y4, '-g')
plt.plot(x, y5, '-b', label='y5, y6')
plt.plot(x, y6, '-b')
plt.plot(x, y7, '-y', label='y7, y8')
plt.plot(x, y8, '-y')
plt.plot(x, y9, '-y', label='y9, y10')
plt.plot(x, y10, '-y')

plt.legend(loc='upper center')
plt.grid()
plt.show()

#micky mouse
import matplotlib.pyplot as plt
import numpy as np

#Tentukan wilayah (domain) diagram Cartesian dan rasio lebar dan tinggi diagram
x = np.linspace(-8,7,100000)
plt.figure(figsize=(9,5.5))

#Tentukan persamaan matematika yang diinginkan
y = x -x -0
y1 = (18-x**2)**0.5
y2 = -(18-x**2)**0.5

y3 = 4 + (4-(x-4.8)**2)**0.5
y4 = 4 - (4-(x-4.8)**2)**0.5

y7 = 4 + (4-(x+4.8)**2)**0.5
y8 = 4 - (4-(x+4.8)**2)**0.5

plt.plot(x, y1, '-k')
plt.plot(x, y2, '-k')
plt.plot(x, y3, '-k')
plt.plot(x, y4, '-k')
plt.plot(x, y7, '-k')
plt.plot(x, y8, '-k')

plt.legend(loc='upper center')
plt.grid()
plt.show()

#objek garis
import numpy as np
import matplotlib.pyplot as plt

ya = 200; xa = 200
yb = 200; xb = 600
yc = 600; xc = 600
yd = 600; xd = 200

pd = int(8); pr = 255; pg = 0; pb = 255
lw = int(8); lr = 255; lg = 0; lb = 255

col = int(800)
row = int(800)
print("col, row =", col, ",", row)

def buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb):
    gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)
    hd = int(pd/2)
    hw = int(lw/2)
    dy = y2-y1
    dx = x2-x1

    for i in range(x1 - hd, x1 * hd):
        for j in range(y1 - hd, y1 * hd):
            if ((i - x1) ** 2 + (j - y1) ** 2) < hd ** 2:
                gambar[j, i, 0] = pr
                gambar[j, i, 1] = pg
                gambar[j, i, 2] = pb

    for i in range(x2 - hd, x2 * hd):
        for j in range(y2 - hd, y2 * hd):
            if ((i - x2) ** 2 + (j - y2) ** 2) < hd ** 2:
                gambar[j, i, 0] = pr
                gambar[j, i, 1] = pg
                gambar[j, i, 2] = pb

    if dy <= dx:
        my = dy / dx
        for i in range(x1, x2):
            j = int(my * (i-x1) + y1)
            x = i
            y = j
            print("x, y =", x, ",", y)
            for i in range(x-hw, x+hw):
                for j in range(y-hw, y+hw):
                    if ((i-x)**2 + (j-y)**2) < hw **2:
                        gambar[j, i, 0] = lr
                        gambar[j, i, 1] = lg
                        gambar[j, i, 2] = lb

    if dy > dx:
        mx = dx / dy
        for j in range(y1, y2):
            i = int(mx * (j-y1) + x1)
            x = i
            y = j
            print("x, y =", x, ",", y)
            for i in range(x-hw, x+hw):
                for j in range(y-hw, y+hw):
                    if ((i-x)**2 + (j-y)**2) < hw **2:
                        gambar[j, i, 0] = lr
                        gambar[j, i, 1] = lg
                        gambar[j, i, 2] = lb

    return gambar

hasil = buat_garis(ya, xa, yb, xb, pd, lw, pr, pg, pb, lr, lg, lb)

plt.figure()
plt.imshow(hasil)
plt.show()

#titik
import numpy as np
import matplotlib.pyplot as plt

# User entries the user informs the coordinates
x1 = 100; y1 = 200
x2 = 700; y2 = 700

# The user decides the line width
lw = int(10)

# Calculate the half line canvas
hw = int(lw/2)

# Setting the size of the canvas
col = int(800)
row = int(800)
print("col, row =", col, ",", row)

# Preparing the lack canvas
gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)
gambar[:, :, :] = 255       # Mengubah layar ke putih

# Warna hijau
hijau = (0, 255, 0)

# Menggambar titik dengan satu piksel
gambar[y1, x1, :] = hijau
gambar[y2, x2, :] = hijau
# gambar[y1, x1, 0] = 255

for i in range(x1-hw, x1+hw):
    for j in range(y1-hw, y1+hw):
        if ((i - x1)**2 + (j-y1)**2) < hw **2:
            gambar[j, i, :] = hijau
            # gambar[j, i, 0] = 255

for i in range(x2-hw, x2+hw):
    for j in range(y2-hw, y2+hw):
        if ((i - x2)**2 + (j-y2)**2) < hw **2:
            gambar[j, i, :] = hijau
            # gambar[j, i, 0] = 255

plt.figure()
plt.imshow(gambar)
plt.show()

#titik garis
import numpy as np
import matplotlib.pyplot as plt

y1 = 600
x1 = 200
y2 = 200
x2 = 600

pd = int(6); pr = 255; pg = 255; pb = 0
lw = int(6); lr = 255; lg = 255; lb = 0

col = int(800)
row = int(800)

def buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb):
    gambar = np.zeros(shape=(row, col, 3), dtype=np.int16)
    hd = int(pd/2)
    hw = int(lw/2)
    dy = y2-y1
    dx = x2-x1

    for i in range(x1 - hd, x1 * hd):
        for j in range(y1 - hd, y1 * hd):
            if ((i - x1) ** 2 + (j - y1) ** 2) < hd ** 2:
                gambar[j, i, 0] = pr
                gambar[j, i, 1] = pg
                gambar[j, i, 2] = pb

    for i in range(x2 - hd, x2 * hd):
        for j in range(y2 - hd, y2 * hd):
            if ((i - x2) ** 2 + (j - y2) ** 2) < hd ** 2:
                gambar[j, i, 0] = pr
                gambar[j, i, 1] = pg
                gambar[j, i, 2] = pb

    if dy <= dx:
        my = dy / dx
        for i in range(x1, x2):
            j = int(my * (i-x1) + y1)
            x = i
            y = j
            print("x, y =", x, ",", y)
            for i in range(x-hw, x+hw):
                for j in range(y-hw, y+hw):
                    if ((i-x)**2 + (j-y)**2) < hw **2:
                        gambar[j, i, 0] = lr
                        gambar[j, i, 1] = lg
                        gambar[j, i, 2] = lb

    if dy > dx:
        mx = dx / dy
        for j in range(y1, y2):
            i = int(mx * (j-y1) + x1)
            x = i
            y = j
            print("x, y =", x, ",", y)
            for i in range(x-hw, x+hw):
                for j in range(y-hw, y+hw):
                    if ((i-x)**2 + (j-y)**2) < hw **2:
                        gambar[j, i, 0] = lr
                        gambar[j, i, 1] = lg
                        gambar[j, i, 2] = lb

    return gambar

hasil = buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb)

plt.figure()
plt.imshow(hasil)
plt.show()