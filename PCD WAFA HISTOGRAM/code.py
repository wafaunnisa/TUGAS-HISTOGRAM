import imageio.v2 as image  
import numpy as np
import matplotlib.pyplot as plt

# Path file gambar (gunakan slash atau raw string untuk path yang benar)
path = r"C:/Users/ACER/Downloads/pexels-shafi_fotumcatcher-1249695-2378278.jpg"

# Membaca gambar
my_image = image.imread(path)

# Memastikan gambar memiliki 3 channel (RGB)
if len(my_image.shape) < 3:
    print("Gambar input harus RGB")
    exit()

# Memisahkan channel RGB
red = my_image[:, :, 0]
green = my_image[:, :, 1]
blue = my_image[:, :, 2]

# Membuat gambar grayscale dengan rata-rata dari tiga channel
gray = (red + green + blue) / 3

# Membuat gambar untuk channel merah
image_red = np.zeros_like(my_image)
image_red[:, :, 0] = red

# Membuat gambar untuk channel hijau
image_green = np.zeros_like(my_image)
image_green[:, :, 1] = green

# Membuat gambar untuk channel biru
image_blue = np.zeros_like(my_image)
image_blue[:, :, 2] = blue

# Membuat gambar grayscale dengan channel RGB
image_gray = np.zeros_like(my_image)
image_gray[:, :, 0] = gray
image_gray[:, :, 1] = gray
image_gray[:, :, 2] = gray

# Menentukan threshold untuk gambar hitam-putih (binary)
threshold_bw = 128
image_bw = np.zeros_like(my_image)
image_bw[gray > threshold_bw] = 255
image_bw[gray <= threshold_bw] = 0

# Mengubah gambar grayscale dan binary ke uint8 sebelum disimpan
image_gray = image_gray.astype("uint8")
image_bw = image_bw.astype("uint8")

# Menyimpan hasil gambar RGB dan grayscale dengan nama file yang berbeda
image.imwrite("C:/Users/ACER/Downloads/Kucing_Persia_Red.jpeg", image_red)
image.imwrite("C:/Users/ACER/Downloads/Kucing_Persia_Green.jpeg", image_green)
image.imwrite("C:/Users/ACER/Downloads/Kucing_Persia_Blue.jpeg", image_blue)
image.imwrite("C:/Users/ACER/Downloads/Kucing_Persia_Gray.jpeg", image_gray)
image.imwrite("C:/Users/ACER/Downloads/Kucing_Persia_BW.jpeg", image_bw)

# Menampilkan informasi dimensi gambar
print(f"Dimensi Gambar Adalah {my_image.shape}")
print("Proses Selesai!")

# Fungsi untuk menampilkan histogram dari setiap channel
def plot_histogram(channel_data, color, title):
    plt.figure(figsize=(10, 6))
    plt.hist(channel_data.ravel(), bins=256, color=color, alpha=0.7)
    plt.title(title)
    plt.xlabel('Intensitas Piksel')
    plt.ylabel('Frekuensi')
    plt.grid(axis='y')
    plt.show()

# Menampilkan histogram untuk masing-masing channel RGB dan grayscale
plot_histogram(red, 'red', 'Histogram Saluran Merah')
plot_histogram(green, 'green', 'Histogram Saluran Hijau')
plot_histogram(blue, 'blue', 'Histogram Saluran Biru')
plot_histogram(gray, 'gray', 'Histogram Gambar Grayscale')
