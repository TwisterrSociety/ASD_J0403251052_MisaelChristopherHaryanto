import os

# Nama file database
nama_file = "data_mahasiswa.txt"

# =================================================================
# Latihan 1: Membuat fungsi Load Data (Membaca file ke Dictionary)
# =================================================================
def baca_data_mahasiswa(nama_file):
    data_dict = {}
    
    # Cek apakah file ada untuk menghindari error
    if not os.path.exists(nama_file):
        # Jika tidak ada, buat file kosong
        open(nama_file, "w").close()
        return data_dict

    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            if not baris: continue
            
            parts = baris.split(",")
            if len(parts) != 3: continue
            
            nim, nama, nilai_str = parts
            data_dict[nim] = {
                "nama": nama,
                "nilai": int(nilai_str)
            }
    return data_dict

# =================================================================
# Fungsi Bantu: Menampilkan Data (Tabel)
# =================================================================
def tampilkan_data(data_dict):
    print("\n=== Daftar Mahasiswa ===")
    print(f"{'NIM':<10} | {'Nama':<12} | {'Nilai':<5}")
    print("-" * 35)
    
    if not data_dict:
        print("Data kosong.")
    else:
        for nim, info in data_dict.items():
            print(f"{nim:<10} | {info['nama']:<12} | {info['nilai']:<5}")
    print("-" * 35)

# =================================================================
# Latihan 3: Membuat fungsi Mencari Data
# =================================================================
def cari_data(data_dict):
    print("\n=== Pencarian Data ===")
    nim_cari = input("Masukkan NIM yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        print("Data Ditemukan:")
        print(f"NIM   : {nim_cari}")
        print(f"Nama  : {data_dict[nim_cari]['nama']}")
        print(f"Nilai : {data_dict[nim_cari]['nilai']}")
    else:
        print("Data tidak ditemukan")

# =================================================================
# Latihan 4 (Bagian 2): Fungsi Menyimpan Data ke File
# =================================================================
def simpan_data(nama_file, data_dict):
    try:
        with open(nama_file, "w", encoding="utf-8") as file:
            for nim, info in data_dict.items():
                line = f"{nim},{info['nama']},{info['nilai']}\n"
                file.write(line)
        print("Data Berhasil Disimpan ke File.")
    except Exception as e:
        print(f"Gagal menyimpan data: {e}")

# =================================================================
# Latihan 5: Fungsi Update Nilai (Hanya di Memori/Dictionary)
# =================================================================
def update_nilai(data_dict):
    print("\n=== Update Nilai Mahasiswa ===")
    nim_update = input("Masukkan NIM mahasiswa yang akan diupdate nilainya: ").strip()
    
    if nim_update not in data_dict:
        print(f"NIM {nim_update} tidak ditemukan, update dibatalkan.")
        return
    
    try:
        nilai_baru = int(input("Masukkan nilai baru (0-100): ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan.")
        return
    
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 sampai 100. Update dibatalkan.")
        return

    nilai_lama = data_dict[nim_update]["nilai"]
    data_dict[nim_update]["nilai"] = nilai_baru

    print(f"Update Berhasil. Nilai {nim_update} berubah dari {nilai_lama} menjadi {nilai_baru}")
4    print("(Catatan: Jangan lupa pilih menu 'Simpan data ke file' agar perubahan tersimpan permanen)")

# =================================================================
# MAIN PROGRAM (MENU LOOP)
# =================================================================

# 1. Load data saat program baru mulai
buka_data = baca_data_mahasiswa(nama_file)

# 2. Jalankan Menu Loop
while True:
    print("\n=== MENU DATA MAHASISWA ===")
    print("1. Tampilkan semua data")
    print("2. Cari data berdasarkan NIM")
    print("3. Update nilai mahasiswa")
    print("4. Simpan data ke file")
    print("0. Keluar")
    
    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == "1":
        tampilkan_data(buka_data)
    
    elif pilihan == "2":
        cari_data(buka_data)
    
    elif pilihan == "3":
        update_nilai(buka_data)
    
    elif pilihan == "4":
        simpan_data(nama_file, buka_data)
    
    elif pilihan == "0":
        print("Terima kasih! Keluar dari program.")
        break
    
    else:
        print("Pilihan tidak valid, silakan coba lagi.")