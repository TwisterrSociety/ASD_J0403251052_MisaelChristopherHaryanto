# ==========================================
# Nama  : Misael Christopher Haryanto
# NIM   : J0403251052
# Kelas : TPL B1
# Tugas : Praktikum 5 - Materi 4 (Backtracking Biner Dasar)
# ==========================================

# Fungsi backtracking untuk menghasilkan semua kombinasi biner sepanjang n
def biner(n, hasil=""):
    # Base case: jika panjang string 'hasil' sudah mencapai n (batas digit), cetak hasilnya.
    if len(hasil) == n:
        print(hasil)
        return
    
    # Choose + Explore cabang kiri: Tambahkan '0' ke dalam string hasil
    # Program akan menelusuri cabang ini sampai selesai (mencapai base case)
    biner(n, hasil + "0")
    
    # Choose + Explore cabang kanan: Tambahkan '1' ke dalam string hasil
    # Program akan menelusuri cabang ini setelah langkah (mundur/backtrack) dari cabang sebelumnya
    biner(n, hasil + "1")

# Memanggil fungsi untuk kombinasi biner 3 digit
biner(3)