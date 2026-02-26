# ==========================================
# Nama  : Misael Christopher Haryanto
# NIM   : J0403251052
# Kelas : TPL B1
# Tugas : Praktikum 5 - Materi 2 (Tracing Rekursi)
# ==========================================

# Fungsi untuk melihat alur stack masuk (stacking) dan keluar (unwinding)
def hitung(n):
    # Base case: Berhenti jika n = 0
    if n == 0:
        print("Selesai")
        return
    
    # Fase Stacking: Bagian ini dieksekusi sebelum pemanggilan rekursif.
    # Data ditumpuk di dalam memori (Call Stack).
    print("Masuk:", n)
    
    # Pemanggilan rekursif
    hitung(n - 1)
    
    # Fase Unwinding: Bagian ini dieksekusi setelah pemanggilan rekursif selesai (mengurai).
    # Tercetak terbalik dari urutan pemanggilan.
    print("Keluar:", n)

# Pemanggilan fungsi
hitung(3)