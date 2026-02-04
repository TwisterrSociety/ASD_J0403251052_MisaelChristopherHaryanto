#========================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 1: Membuat fungsi Load Data
#========================================

nama_file = "data_mahasiswa.txt"

# Membuat fungsi membaca data mahasiswa
def baca_data_mahasiswa(nama_file):
    data_dict = {}  # Buat variable untuk dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()  # menghilangkan karakter baris baru
            parts = baris.split(",")  # perbaikan: gunakan split dengan titik
            if len(parts) != 3:
                continue
            nim, nama, nilai_str = parts
            nilai_int = int(nilai_str)

            # Simpan data mahasiswa ke dictionary dengan key NIM 
            data_dict[nim] = {              # key
                "nama": nama,               # values
                "nilai": nilai_int          # values
            }
    return data_dict   # return harus di luar loop

print("=== Data Mahasiswa dalam Dictionary ===")

# Memanggil fungsi membaca data mahasiswa
buka_data = baca_data_mahasiswa(nama_file)
print("Jumlah data terbaca:", len(buka_data))

# Fungsi menampilkan data mahasiswa
def tampilkan_data(data_dict):
    # Membuat Header Tabel
    print("\n=== Daftar Mahasiswa ===")
    print(f"{'NIM':<10} | {'Nama':<12} | {'Nilai':<5}")
    print("-" * 32)

    '''
    untuk tampilan yang rapi, atur f-string formating
    '''

    # Menampilkan isi dictionary
    for nim, info in data_dict.items():
        print(f"{nim:<10} | {info['nama']:<12} | {info['nilai']:<5}")

# Panggil fungsi tampilkan_data
tampilkan_data(buka_data)
