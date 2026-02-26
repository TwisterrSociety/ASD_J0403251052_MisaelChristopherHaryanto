# ==========================================
# Nama  : Misael Christopher Haryanto
# NIM   : J0403251052
# Kelas : TPL B1
# Tugas : Praktikum 5 - Latihan 2 (Tracing Rekursi)
# ==========================================

def countdown(n):
    # Base case: Kondisi berhenti jika n mencapai 0
    if n == 0:
        print("Selesai")
        return
    
    # Fase Stacking (Masuk): Dieksekusi SEBELUM pemanggilan rekursif
    print("Masuk:", n)
    
    # Recursive call: Memanggil fungsi untuk angka yang lebih kecil
    countdown(n - 1)
    
    # Fase Unwinding (Keluar): Dieksekusi SETELAH pemanggilan rekursif selesai/kembali
    print("Keluar:", n)

# Pemanggilan fungsi utama
countdown(3)

"""
==========================================
JAWABAN DISKUSI LATIHAN 2
==========================================
Diskusi dan jelaskan: Mengapa output 'Keluar' muncul terbalik?

Output 'Keluar' muncul terbalik (Keluar: 1, Keluar: 2, Keluar: 3) karena 
fungsi rekursif bekerja menggunakan prinsip Call Stack (tumpukan) yang 
bersifat LIFO (Last In, First Out). 

Saat `countdown(3)` dipanggil, ia mencetak "Masuk: 3", lalu memanggil `countdown(2)`. 
Fungsi `countdown(3)` ini "ditahan" (belum selesai) karena menunggu hasil dari `countdown(2)`. 
Hal ini terus berlanjut hingga `countdown(1)` memanggil `countdown(0)`.

Ketika `countdown(0)` dieksekusi (base case tercapai), fungsi berhenti memanggil dirinya 
dan kembali (return) ke fungsi yang memanggilnya terakhir kali, yaitu `countdown(1)`. 
Barulah `countdown(1)` bisa melanjutkan baris kode berikutnya, yaitu mencetak "Keluar: 1". 
Setelah itu tumpukan terurai kembali ke atas untuk `countdown(2)` dan `countdown(3)`.
"""