"""
Nama  : Misael Christopher Haryanto
NIM   : J0403251052
Kelas : TPL B1

Praktikum 6 - Latihan 1
Memahami Kode Program Insertion Sort
"""

def insertion_sort(data):
    """
    Fungsi ini melakukan pengurutan data menggunakan algoritma Insertion Sort
    secara ascending (dari kecil ke besar).
    """

    # Perulangan dimulai dari indeks 1
    # karena indeks 0 dianggap sudah terurut
    for i in range(1, len(data)):

        key = data[i]  # key adalah elemen yang akan disisipkan
        j = i - 1      # j adalah indeks elemen sebelumnya

        # Selama elemen di kiri lebih besar dari key,
        # maka geser ke kanan
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]  # Geser elemen ke kanan
            j -= 1

        # Letakkan key di posisi yang benar
        data[j + 1] = key

    return data


# ================== JAWABAN SOAL ==================

"""
1. Mengapa perulangan dimulai dari indeks 1?
   Karena elemen pertama (index 0) dianggap sudah terurut.
   Pengurutan dimulai dari elemen kedua.

2. Apa fungsi variabel key?
   Key berfungsi sebagai nilai yang akan dibandingkan
   dan disisipkan ke posisi yang benar.

3. Mengapa digunakan while bukan for?
   Karena jumlah pergeseran tidak pasti.
   While digunakan selama kondisi masih terpenuhi.

4. Operasi apa yang terjadi di dalam while?
   Terjadi pergeseran elemen ke kanan
   jika elemen sebelumnya lebih besar dari key.
"""

# ================== TEST RUN ==================

data = [5, 2, 4, 6, 1, 3]
print("Data sebelum sorting:", data)
print("Data setelah sorting :", insertion_sort(data))