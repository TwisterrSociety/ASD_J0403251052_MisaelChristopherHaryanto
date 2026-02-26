#========IDENTITAS MAHASISWA===================
# Nama  : Misael Christopher Haryanto
# NIM   : J0403251052
# Kelas : TPL B1
#==============================================

# Studi Kasus (Contoh): Sistem Antrian Layanan Akademik
# Struktur Data: Queue (FIFO) berbasis Linked List

# 1) Definisi Node (unit dasar Linked List)
class Node:
    def __init__(self, nim, nama):
        self.nim = nim      # menyimpan NIM mahasiswa
        self.nama = nama    # menyimpan nama mahasiswa
        self.next = None    # pointer ke node berikutnya (awal: None)

# 2) Definisi Queue berbasis Linked List
# front: node paling depan (yang dilayani lebih dulu)
# rear: node paling belakang (tempat masuk data baru)
class QueueAkademik:
    def __init__(self):
        self.front = None   # queue awalnya kosong
        self.rear = None

    def is_empty(self):
        # Queue kosong jika front = None
        return self.front is None

    def enqueue(self, nim, nama):
        """Menambah mahasiswa ke BELAKANG antrian (rear)."""
        node_baru = Node(nim, nama) # 1) buat node baru
        
        # 2) Jika queue kosong, front dan rear menunjuk node baru
        if self.is_empty():
            self.front = node_baru
            self.rear = node_baru
            return

        # 3) Jika queue tidak kosong:
        # rear lama menunjuk node baru, lalu rear berpindah ke node baru
        self.rear.next = node_baru
        self.rear = node_baru

    def dequeue(self):
        """Melayani (mengambil & menghapus) mahasiswa dari DEPAN antrian (front)."""
        if self.is_empty():
            print("Antrian kosong. Tidak ada mahasiswa yang bisa dilayani.")
            return None
        
        # 1) Ambil node paling depan
        node_dilayani = self.front
        
        # 2) Geser front ke node berikutnya
        self.front = self.front.next
        
        # 3) Jika setelah geser front menjadi None, berarti queue kosong
        # sehingga rear juga harus None
        if self.front is None:
            self.rear = None
            
        return node_dilayani

    def tampilkan(self):
        """Menampilkan seluruh isi antrian dari front ke rear."""
        if self.is_empty():
            print("Antrian kosong.")
            return
            
        print("\nDaftar Antrian Mahasiswa (Front -> Rear):")
        current = self.front
        no = 1
        
        # Traversal dari front sampai None
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next
            no += 1

# 3) Program Utama (Menu Interaktif)
def main():
    q = QueueAkademik() # membuat objek antrian
    
    while True:
        print("\n=== Sistem Antrian Akademik ===")
        print("1. Tambah Mahasiswa (Enqueue)")
        print("2. Layani Mahasiswa (Dequeue)")
        print("3. Lihat Antrian")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ").strip()
        
        if pilihan == "1":
            nim = input("Masukkan NIM : ").strip()
            nama = input("Masukkan Nama: ").strip()
            
            # Validasi sederhana input kosong
            if nim == "" or nama == "":
                print("NIM dan Nama tidak boleh kosong.")
                continue
                
            q.enqueue(nim, nama)
            print("Mahasiswa berhasil ditambahkan ke antrian.")
            
        elif pilihan == "2":
            node = q.dequeue()
            if node is not None:
                print(f"Mahasiswa dilayani: {node.nim} - {node.nama}")
                
        elif pilihan == "3":
            q.tampilkan()
            
        elif pilihan == "4":
            print("Program selesai. Terima kasih.")
            break
            
        else:
            print("Pilihan tidak valid. Silakan pilih 1-4.")

# 4) Penanda eksekusi file utama
if __name__ == "__main__":
    main()