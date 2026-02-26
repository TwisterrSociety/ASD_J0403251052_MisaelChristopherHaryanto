# ==========================================
# Nama  : Misael Christopher Haryanto
# NIM   : J0403251052
# Kelas : TPL B1
# Tugas : Praktikum 5 - Latihan 5 (Generator PIN)
# ==========================================

def buat_pin(panjang, hasil=""):
    # Base case: Jika panjang PIN yang sedang dibuat sudah sesuai dengan target
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    
    # Loop untuk mencoba setiap kemungkinan angka (0, 1, 2) - Choose
    for angka in ["0", "1", "2"]:
        # Mencegah angka yang sama muncul berulang (Jawaban Diskusi)
        # HAPUS ATAU KOMENTARI 2 BARIS DI BAWAH JIKA INGIN PIN BOLEH BERULANG
        # (seperti "000" atau "112")
        if angka in hasil:
            continue # Pruning: Lewati angka ini jika sudah ada di dalam variabel 'hasil'
            
        # Recursive call: Tambahkan angka yang dipilih ke hasil dan lanjut ke digit berikutnya (Explore)
        buat_pin(panjang, hasil + angka)

# Memanggil fungsi untuk membuat PIN sepanjang 3 digit
buat_pin(3)

"""
==========================================
JAWABAN DISKUSI LATIHAN 5
==========================================
Diskusi dan jelaskan: Bagaimana cara mencegah angka yang sama muncul berulang?

Untuk mencegah angka yang sama muncul berulang (misalnya mencegah "000", "011"), 
kita menggunakan teknik "Pruning" (Pemangkasan) di dalam algoritma backtracking. 


Caranya adalah dengan menambahkan pengecekan kondisi (if) di dalam perulangan `for` sebelum 
melakukan pemanggilan fungsi rekursif (explore). 

Sintaks yang ditambahkan:
    if angka in hasil:
        continue
        
Penjelasan: Sebelum menambahkan `angka` ke dalam string `hasil`, program mengecek apakah 
angka tersebut sudah pernah digunakan di dalam string `hasil`. Jika sudah ada (True), 
maka program memanggil instruksi `continue` untuk melewati sisa blok perulangan tersebut 
(memangkas cabang pohon keputusan) dan beralih menguji angka berikutnya. 
Ini menjamin bahwa output yang dihasilkan hanya berupa kombinasi angka yang unik (permutasi tanpa pengulangan).
"""