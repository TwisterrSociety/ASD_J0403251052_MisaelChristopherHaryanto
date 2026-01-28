#===================================================
#praktikum 1: konsep ADT dan file handling
#Latihan Dasar 1A: Membaca seluruh isi file
#===================================================

#membuka file dengan mode read ("r")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)

print("===Hasil Read===")
print("Tipe Data:", type(isi_file))
print("Jumlah Karakter:", len(isi_file))
print("Jumlah Baris:", isi_file.count("\n")+1)

#membuka file per baris
print("===Membaca file per baris===")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #menghilangkan
        print("Baris ke:", jumlah_baris)
        print("Isinya:", baris)