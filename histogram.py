
import numpy as np #Mengimport library numpy kemudian di inisialisasi dengan np
import imageio.v3 as imageio # Mengimport library dari imageio
import cv2 as cv #Memasukan atau mengimport library dari cv2
import matplotlib.pyplot as plt #Mengimport pyplot dari matplotlib kemudian di inisialisasi dengan plt

img = plt.imread(r'C:\Users\ASUS\Documents\FILE SYAHDAN\semester 6\PCD\pertemuan 7\Saitama.JPG')#Membaca gambar format JPEG dengan kode plt dan disimpan dalam variabel img


#Mendapatkan/define resolusi dan tipe gambar
img_height = img.shape[0]#Tinggi gambar disimpan pada variabel img.shape 0
img_width = img.shape[1]#Panjang gambar disimpan pada variabel img.shape 1
img_channel = img.shape[2]# Warna Channel gambar disimpan pada variabel img.shape 2

#Merubah gambar menjadi Grayscale
img_grayscale = np.zeros(img.shape, dtype=np.uint8)# digunakan untuk membuat array berukuran sama dengan gambar asli, dengan nilai awal 0 dan tipe data unsigned integer 8 bit

for y in range(0, img_height):#Pengunlangan iterasi y pada variabel img_height
    for x in range(0, img_width):#Pengunlangan iterasi x pada variabel img_width
        red = img[y][x][0]#Mendapatkan itensitas warna merah
        green = img[y][x][1]#Mendapatkan itensitas warna hijau
        blue = img[y][x][2]#Mendapatkan itensitas warna biru
        gray = (int(red) + int(green) + int(blue)) / 3
        img_grayscale[y][x] = (gray, gray, gray) #Berisi pengaturan untuk mengubah itensitas warna RGB ke Grayscale
        
plt.imshow(img_grayscale)#Menampilkan gambar pada variabel img_grayscale hasil perubahan 
plt.title("Grayscale")#Menampilkan judul gambar
plt.show()#Membantu menampilkan gambar

hg = np.zeros((256))#Membuat variabel untuk menyimpan data gambar

for x in range(0, 256):#
    hg[x] = 0#Mengisi setiap nilai dalam array hg dengan 0
#Menghitung nilai dari gambar    
for y in range(0, img_height):#Pengulangan iterasi y pada variabel img_height
    for x in range(0, img_width):#Pengulangan iterasi x pada variabel img_width
        gray = img_grayscale[y][x][0]#Mengakses piksel di koordinat x dan y dan mengambil itensitas warna ke-) dalam piksel dan menyimpannya dalam variabel gray 
        hg[gray] += 1   #Mengisi array pada variabel gray dengan 1 (hanya ada satu piksel)
        
# plt.figure(figsize=(20, 6))
# plt.plot(hg, color="black", linewidth=2.0)
# plt.show()
#Menampilkan Histogram
bins = np.linspace(0, 256, 100)#Membuat batasan pada array
plt.hist(hg, bins, color="black", alpha=0.5)#Membuat histogram dengan batasan array dan membrikan warna hitam serta memberikan tingkat transparansi
plt.title("Histogram")#Menampilakn judul pada histogram
plt.show()
#Membuat variabel untuk menyimpan data gambar
hgr = np.zeros((256))
hgg = np.zeros((256))
hgb = np.zeros((256))
hgrgb = np.zeros((768))  
#Mengisi setiap nilai dalam array hg dengan 0
for x in range(0, 256): #Pengunlangan iterasi x sebanyak 0 kali pada array 256 piksel
    hgr[x] = 0
    hgg[x] = 0
    hgb[x] = 0
    
for x in range(0, 768): #Pengunlangan iterasi y sebanyak 0 kali pada array 768 piksel
    hgrgb[x] = 0       

#Menghitung nilai dari gambar
for x in range(0, 256):
    hgr[x] = 0
    hgg[x] = 0
    hgb[x] = 0
    
for x in range(0, 768):
    hgrgb[x] = 0

# th = int(256/64)
temp = [0]
for y in range(0, img.shape[0]):#Pengulangan iterasi y pada variabel img_shape 0
    for x in range(0, img.shape[1]):#Pengulangan iterasi y pada variabel img_shape 1
        red = int(img[y][x][0])#Mendapatkan itensitas warna merah
        green = int(img[y][x][1])#Mendapatkan itensitas warna hijau
        blue = int(img[y][x][2])#Mendapatkan itensitas warna biru
        green = green + 256#Mengubah itensitas warna hijau dengan menambah 256
        blue = blue + 512#Mengubah itensitas warna hijau dengan menambah 512
#         temp.append(green)
        #Menambahkan 1 setiap varibel RGB untuk menyimpan histogram pada hgrgb
        hgrgb[red] += 1 
        hgrgb[green] += 1
        hgrgb[blue] += 1

binsrgb = np.linspace(0, 768, 100)#Membuat batasan pada array
plt.hist(hgrgb, binsrgb, color="black", alpha=0.5)#Membuat histogram dengan batasan array dan membrikan warna hitam serta memberikan tingkat transparansi
# plt.plot(hgrgb)
plt.title("Histogram Red Green Blue")#Memberikan judul pada histogram
plt.show()#Menampilkan histogram     
#Menampilkan Histogram
for y in range(0, img_height):#Pengulangan iterasi y pada variabel img_height
    for x in range(0, img_width):#Pengulangan iterasi x pada variabel img_width
        red = img[y][x][0]#Mendapatkan itensitas warna merah
        green = img[y][x][1]#Mendapatkan itensitas warna hijau
        blue = img[y][x][2]#Mendapatkan itensitas warna biru
        #Menambahkan 1 setiap varibel RGB untuk menyimpan histogram pada hgrgb
        hgr[red] += 1
        hgg[green] += 1
        hgb[blue] += 1

bins = np.linspace(0, 256, 100)#Membuat batasan pada array
plt.hist(hgr, bins, color="red", alpha=0.5)##Membuat histogram dengan batasan array dan membrikan warna hitam serta memberikan tingkat transparansi
plt.title("Histogram Red")#Memberikan judul pada histogram 
plt.show()#Menampilkan histogram

plt.hist(hgg, bins, color="green", alpha=0.5)#Membuat histogram dengan batasan array dan membrikan warna hitam serta memberikan tingkat transparansi
plt.title("Histogram Green")#Memberikan judul pada histogram 
plt.show()#Menampilkan histogram

plt.hist(hgb, bins, color="blue", alpha=0.5)#Membuat histogram dengan batasan array dan membrikan warna hitam serta memberikan tingkat transparansi
plt.title("Histogram Blue")#Memberikan judul pada histogram 
plt.show()#Menampilkan histogram
#Menampilkan Histogram Kumulatif
hgk = np.zeros((256))
c = np.zeros((256))

for x in range(0, 256):
    hgk[x] = 0
    c[x] = 0

for y in range(0, img_height):
    for x in range(0, img_width):
        gray = img_grayscale[y][x][0]
        hgk[gray] += 1
                
c[0] = hgk[0]
for x in range(1, 256):
     c[x] = c[x-1] + hgk[x]

hmaxk = c[255]

for x in range(0, 256):
    c[x] = 190 * c[x] / hmaxk

plt.hist(c, bins, color="black", alpha=0.5)#Membuat histogram dengan batasan array dan membrikan warna hitam serta memberikan tingkat transparansi
plt.title("Histogram Grayscale Kumulatif")#Memberikan judul pada histogram 
plt.show()#Menampilkan histogram

#Menampilkan Histogram Hequalisasi
hgh = np.zeros((256))
h = np.zeros((256))
c = np.zeros((256))

for x in range(0, 256): 
    hgh[x] = 0
    h[x] = 0
    c[x] = 0

for y in range(0, img_height):
    for x in range(0, img_width):
        gray = img_grayscale[y][x][0]
        hgh[gray] += 1
                
h[0] = hgh[0]
for x in range(1, 256):
     h[x] = h[x-1] + hgh[x]

for x in range(0, 256):
     h[x] = h[x] / img_height / img_width

for x in range(0, 256):
    hgh[x] = 0
    
for y in range(0, img_height):
    for x in range(0, img_width):
        gray = img_grayscale[y][x][0]
        gray = h[gray] * 255
        hgh[int(gray)] += 1

c[0] = hgh[0]
for x in range(1, 256):
     c[x] = c[x-1] + hgh[x]

hmaxk = c[255]

for x in range(0, 256):
    c[x] = 190 * c[x] / hmaxk

plt.hist(c, bins, color="black", alpha=0.5)#Membuat histogram dengan batasan array dan membrikan warna hitam serta memberikan tingkat transparansi
plt.title("Histogram Grayscale Hequalisasi")#Memberikan judul pada histogram 
plt.show()

