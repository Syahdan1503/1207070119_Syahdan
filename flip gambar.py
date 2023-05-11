
import numpy as np #Mengimport library numpy kemudian di inisialisasi dengan np
import imageio.v3 as imageio # Mengimport library dari imageio
import cv2 as cv #Memasukan atau mengimport library dari cv2
import matplotlib.pyplot as plt #Mengimport pyplot dari matplotlib kemudian di inisialisasi dengan plt

img = plt.imread(r'C:\Users\ASUS\Documents\FILE SYAHDAN\semester 6\PCD\pertemuan 7\Saitama.JPG')#Membaca gambar format JPEG dengan kode plt dan disimpan dalam variabel img


#Mendapatkan/define resolusi dan tipe gambar
img_height = img.shape[0]#Tinggi gambar disimpan pada variabel img.shape 0
img_width = img.shape[1]#Panjang gambar disimpan pada variabel img.shape 1
img_channel = img.shape[2]# Warna Channel gambar disimpan pada variabel img.shape 2
img_type = img.dtype#Tipe gambar disimpan pada variabel img.dtype

#Membuat variabel dengan resolusi dan tipe yang sama seperti gambar
img_flip_horizontal = np.zeros(img.shape, img_type)
img_flip_vertical = np.zeros(img.shape, img_type)

#Membalik gambar secara horizontal
for y in range(0, img_height):#Pengunlangan iterasi y pada variabel img_height
    for x in range(0, img_width):#Pengulangan iterasi x pada variabel img_widhy
        for c in range(0, img_channel):#Pengulangan iterasi c pada variabel img_channel
            img_flip_horizontal[y][x][c] = img[y][img_width-1-x][c]#Berisi pengaturan untuk memirror gambar menjadi horizontal
#Membalik gambar secara vertical
for y in range(0, img_height):#Pengunlangan iterasi y pada variabel img_height
    for x in range(0, img_width):#Pengulangan iterasi x pada variabel img_widhy
        for c in range(0, img_channel):#Pengulangan iterasi c pada variabel img_channel
            img_flip_vertical[y][x][c] = img[img_height-1-y][x][c]#Berisi pengaturan untuk memirror gambar menjadi vertical
            
#Menampilkan hasil balik gambar            
plt.imshow(img_flip_horizontal)#Menampilkan gambar pada variabel img_flip_horizontal
plt.title("Flip Horizontal")#Memberikan judul pada gambar yang ditampilkan
plt.show()#Membantu menampilkan gambar
plt.imshow(img_flip_vertical)#Menampilkan gambar pada variabel img_flip_vertikal
plt.title("Flip Vertical")#Memberikan judul pada gambar yang ditampilkan
plt.show()#Membantu menampilkan gambar
