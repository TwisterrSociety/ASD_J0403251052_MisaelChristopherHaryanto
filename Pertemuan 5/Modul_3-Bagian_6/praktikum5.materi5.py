# ==========================================
# Nama  : Misael Christopher Haryanto
# NIM   : J0403251052
# Kelas : TPL B1
# Tugas : Praktikum 5 - Materi 5 (Backtracking dengan Pruning)
# ==========================================

# Fungsi backtracking kombinasi biner dengan batas maksimal kemunculan angka '1'
def biner_batas(n, batas, hasil="", jumlah_1=0):
    # Pruning (Pemangkasan): Menghentikan pencarian jika jumlah angka '1' 
    # sudah melewati batas maksimal yang ditentukan. Cabang ini tidak akan diteruskan.
    if jumlah_1 > batas:
        return
        
    # Base case: jika panjang string 'hasil' sudah n, cetak hasilnya
    if len(hasil) == n:
        print(hasil)
        return
        
    # Pilih '0': Tambahkan 0, jumlah '1' tidak bertambah
    biner_batas(n, batas, hasil + "0", jumlah_1)
    
    # Pilih '1': Tambahkan 1, nilai parameter jumlah_1 bertambah 1
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)

# Memanggil fungsi untuk kombinasi biner 4 digit, tapi angka '1' maksimal muncul 2 kali
biner_batas(4, 2)