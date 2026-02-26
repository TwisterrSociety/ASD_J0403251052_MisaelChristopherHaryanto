# ==========================================
# Nama  : Misael Christopher Haryanto
# NIM   : J0403251052
# Kelas : TPL B1
# Tugas : Praktikum 5 - Latihan 3 (Cari Nilai Maksimum List)
# ==========================================

def cari_maks(data, index=0):
    # Base case: Jika index sudah berada di elemen terakhir list
    # kembalikan elemen tersebut sebagai nilai maksimum (sementara).
    if index == len(data) - 1:
        return data[index]
    
    # Recursive call: Cari nilai maksimum dari sisa list di sebelah kanannya
    maks_sisa = cari_maks(data, index + 1)
    
    # Bandingkan elemen saat ini (data[index]) dengan nilai maksimum dari sisa list
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa

# Inisialisasi list data angka
angka = [3, 7, 2, 9, 5]

# Menjalankan fungsi dan mencetak hasilnya
print("Nilai maksimum:", cari_maks(angka))

"""
==========================================
JAWABAN DISKUSI LATIHAN 3
==========================================
Diskusi dan jelaskan alur program serta base case dan recursive call:

1. Alur Program:
   Program membaca list dari kiri ke kanan menggunakan pointer 'index'. 
   Ia membandingkan nilai pada index saat ini dengan "nilai maksimum dari sisa list 
   di sebelah kanannya" yang didapatkan melalui proses rekursif (bottom-up/unwinding).
   
2. Base Case: 
   `if index == len(data) - 1: return data[index]`. 
   Program berhenti memanggil dirinya sendiri saat index mencapai elemen terakhir list. 
   Elemen terakhir tersebut dikembalikan ke atas untuk mulai dibandingkan.

3. Recursive Call: 
   `maks_sisa = cari_maks(data, index + 1)`. 
   Fungsi memanggil dirinya sendiri sambil menggeser index ke kanan (+1) untuk 
   memeriksa elemen list berikutnya, menumpuk (stacking) proses pembandingan 
   sampai mencapai base case.
"""