# ==========================================
# Nama  : Misael Christopher Haryanto
# NIM   : J0403251052
# Kelas : TPL B1
# Tugas : Praktikum 5 - Materi 3 (Jumlah List Rekursif)
# ==========================================

# Fungsi untuk menjumlahkan semua elemen dalam list menggunakan rekursi
def jumlah_list(data, index=0):
    # Base case: jika index sudah mencapai panjang list (out of bounds),
    # hentikan rekursi dan kembalikan nilai 0.
    if index == len(data):
        return 0
    
    # Recursive case: elemen pada index sekarang ditambahkan dengan 
    # hasil penjumlahan sisa elemen setelahnya (menggeser index + 1).
    return data[index] + jumlah_list(data, index + 1)

# Mencetak hasil penjumlahan elemen list [2, 4, 6, 8]
print(jumlah_list([2, 4, 6, 8])) # Output: 20