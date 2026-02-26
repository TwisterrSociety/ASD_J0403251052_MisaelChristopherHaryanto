 q  # ==========================================
# Nama  : Misael Christopher Haryanto
# NIM   : J0403251052
# Kelas : TPL B1
# Tugas : Praktikum 5 - Latihan 1 (Rekursi Pangkat)
# ==========================================

def pangkat(a, n):
    # Base case: Kondisi berhenti ketika pangkat (n) mencapai 0.
    # Nilai apapun yang dipangkatkan 0 hasilnya adalah 1.
    if n == 0:
        return 1
    
    # Recursive case: Mengalikan angka dasar (a) dengan hasil pemanggilan 
    # fungsi pangkat itu sendiri, dengan nilai pangkat (n) dikurangi 1.
    return a * pangkat(a, n - 1)

# Pemanggilan fungsi utama untuk 2 pangkat 4
print("Hasil 2 pangkat 4 adalah:", pangkat(2, 4))

"""
==========================================
JAWABAN DISKUSI LATIHAN 1
==========================================
Diskusi dan jelaskan alur program serta base case dan recursive call:

1. Alur Program:
   Program akan memecah operasi 2^4 menjadi: 2 * (2^3).
   Kemudian 2^3 dipecah menjadi 2 * (2^2), dan seterusnya hingga n=0.
   Ketika n=0 (base case tercapai), fungsi mengembalikan nilai 1 ke pemanggil sebelumnya.
   Lalu hasil dikalikan mundur: 1 * 2 * 2 * 2 * 2 = 16.

2. Base Case: 
   `if n == 0: return 1`. Ini sangat penting agar fungsi rekursif 
   tidak memanggil dirinya sendiri secara terus-menerus (infinite loop).

3. Recursive Call: 
   `return a * pangkat(a, n - 1)`. Ini adalah bagian di mana fungsi 
   memanggil dirinya sendiri dengan ukuran masalah yang diperkecil (n dikurangi 1).
"""