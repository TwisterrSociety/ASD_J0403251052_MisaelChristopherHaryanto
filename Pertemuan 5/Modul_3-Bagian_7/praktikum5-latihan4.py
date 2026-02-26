# ==========================================
# Nama  : Misael Christopher Haryanto
# NIM   : J0403251052
# Kelas : TPL B1
# Tugas : Praktikum 5 - Latihan 4 (Kombinasi Huruf)
# ==========================================

def kombinasi(n, hasil=""):
    # Base case: Jika panjang string 'hasil' sudah sama dengan 'n' (batas yang diinginkan)
    # maka cetak hasilnya dan lakukan backtrack (kembali ke langkah sebelumnya).
    if len(hasil) == n:
        print(hasil)
        return
    
    # Choose + Explore cabang 1: Tambahkan huruf "A" ke dalam string hasil
    kombinasi(n, hasil + "A")
    
    # Choose + Explore cabang 2: Tambahkan huruf "B" ke dalam string hasil
    kombinasi(n, hasil + "B")

# Memanggil fungsi untuk mencari kombinasi dengan panjang 2 karakter
kombinasi(2)

"""
==========================================
JAWABAN DISKUSI LATIHAN 4
==========================================
Diskusi dan jelaskan: bagaimana jumlah kombinasi yang dihasilkan.

Jumlah kombinasi yang dihasilkan mengikuti rumus 2^n. 
Karena ada 2 pilihan huruf ('A' dan 'B') dan panjang kombinasi yang diminta adalah n = 2, 
maka total kombinasi yang dihasilkan adalah 2^2 = 4 kombinasi.

Algoritma backtracking ini membentuk struktur seperti pohon keputusan (Decision Tree). 
Dari titik awal (string kosong), program akan bercabang dua (pilih A atau pilih B). 
Dari masing-masing cabang tersebut, program bercabang dua lagi. 
Sehingga menghasilkan output: AA, AB, BA, BB.
"""