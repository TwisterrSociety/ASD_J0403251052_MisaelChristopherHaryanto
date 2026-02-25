#=======================================
# Nama :
# NIM  :
# Kelas:
#=======================================

#=======================================
# Studi Kasus : Sistem Antrian Layanan Akademik
# Implementasi Queue dengan Linked List
#=======================================

# 1) Node (unit dasar Linked List)
class Node:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.next = None   # ✅ FIX

# 2) Queue Akademik
class QueueAkademik:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, nim, nama):
        nodeBaru = Node(nim, nama)

        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
        else:
            self.rear.next = nodeBaru
            self.rear = nodeBaru

        print("Mahasiswa berhasil ditambahkan ke antrian")

    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong. Tidak ada mahasiswa yang dilayani")
            return None

        node_dilayani = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return node_dilayani

    def tampilkan(self):
        if self.is_empty():
            print("Antrian masih kosong")
            return

        print("\nDaftar Antrian Mahasiswa (Front -> Rear)")
        current = self.front
        no = 1
        while current:
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next
            no += 1

# ================= PROGRAM UTAMA =================
def main():
    q = QueueAkademik()

    while True:
        print("\n=== Sistem Antrian Akademik ===")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "1":
            nim = input("Masukkan NIM  : ").strip()
            nama = input("Masukkan Nama: ").strip()
            q.enqueue(nim, nama)

        elif pilihan == "2":
            dilayani = q.dequeue()
            if dilayani:
                print(f"Mahasiswa dilayani: {dilayani.nim} - {dilayani.nama}")

        elif pilihan == "3":
            q.tampilkan()

        elif pilihan == "4":
            print("Program selesai. Terima kasih 🙏")
            break   # ✅ FIX

        else:
            print("Pilihan tidak valid. Silakan pilih 1-4")

# ================= PENANDA =================
if __name__ == "__main__":
    main()