import imageio.v2 as io
import numpy as np
import matplotlib.pyplot as plt

img = io.imread('Rizki.jpg')
#mendapatkan define resolusi dan tipe gambar
img_height=img.shape[0]
img_width=img.shape[1]
img_channel=img.shape[2]
img_type=img.dtype

img_brightness=np.zeros(img.shape,dtype=np.uint8)
def brighter(nilai):
    for y in range(0,img_height):
        for x in range (0,img_width):
            red=img[y][x][0]
            green=img[y][x][1]
            blue=img[y][x][2]
            gray=(int(red)+int(green)+int(blue))/3
            gray+=nilai
            if gray>255:
                gray=255
            if gray<0:
                gray=0
            img_brightness[y][x]=(gray,gray,gray)

brighter(-100)
plt.imshow(img_brightness)
plt.title("Brightness -100")
plt.show()

brighter(100)
plt.imshow(img_brightness)
plt.title("Brightness 100")
plt.show()
#brightness RGB
#membuat variabel img_rgbbrightness untuk menampung hasil
img_rgbbright = np.zeros(img.shape, dtype = np.uint8)

#melakukan penambahan brightness dengan nilai yg menjadi parameter
def rgbbrighter(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red     = img[y][x][0]
            red     += nilai
            if red > 255:
                red = 255
            if red < 0:
                red = 0
            green   = img[y][x][1]
            green     += nilai
            if green > 255:
                green = 255
            if green < 0:
                green = 0
            blue    = img[y][x][2]
            blue    += nilai
            if blue > 255:
                blue = 255
            if blue < 0:
                blue = 0
            img_rgbbright[y][x] = (red, green, blue)

#menampilkan beberapa hasil dengan nilai brightness -100 dan 100
rgbbrighter(-100)
plt.imshow(img_rgbbright)
plt.title('Brightness -100')
plt.show()

rgbbrighter(100)
plt.imshow(img_rgbbright)
plt.title('Brightness 100')
plt.show()
#contrast

#Membuat variabel img_contrass untuk menampung hasil
img_contrass = np.zeros(img.shape, dtype = np.uint8)

#Melakukan penambahan contrass dengan nilai yg menjadi parameter
def contrass(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red     = img[y][x][0]
            green   = img[y][x][1]
            blue    = img[y][x][2]
            gray    = (int(red) + int(green) + int(blue))/3
            gray    += nilai
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_contrass[y][x] = (gray, gray, gray)

#Menampilkan beberapa hasil dengan nilai contrass 2 dan 25
contrass(2)
plt.imshow(img_contrass)
plt.title('Contrass 2')
plt.show()

contrass(25)
plt.imshow(img_contrass)
plt.title('Contrass 25')
plt.show()
#contrass Auto level
img_autocontrass = np.zeros(img.shape, dtype=np.uint8)
def autocontrass():
    xmax = 300
    xmin = 0
    d = 0
    # Mendapatkan nilai d, dimana nilai d ini akan berpengaruh pada hitungan
    # untuk mendapatkan tingkat kontras
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            if gray < xmax:
                xmax = gray
            if gray > xmin:
                xmin = gray
    d = xmin-xmax
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(float(255/d) * (gray-xmax))
            img_autocontrass[y][x] = (gray, gray, gray)
autocontrass()
plt.imshow(img_autocontrass)
plt.title("Contrass Autolevel")
plt.show()