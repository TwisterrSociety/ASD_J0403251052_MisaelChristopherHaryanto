#========IDENTITAS MAHASISWA===================
# Nama  : Misael Christopher Haryanto
# NIM   : J0403251052
# Kelas : TPL B1
#==============================================

# Tugas Hands-On: Sistem Antrian Bengkel Motor
# ==============================================

class Node:
    def __init__(self, no, nama, servis):
        self.no = no          # Nomor Antrian
        self.nama = nama      # Nama Pelanggan
        self.servis = servis  # Jenis Servis
        self.next = None      # Pointer ke pelanggan berikutnya

class QueueBengkel:
    def __init__(self):
        self.front = None     # Pelanggan paling depan
        self.rear = None      # Pelanggan paling belakang

    def is_empty(self):
        # Cek apakah antrian kosong
        return self.front is None

    def enqueue(self, no, nama, servis):
        # TODO: Tambahkan data ke antrian (Belakang/Rear)
        node_baru = Node(no, nama, servis)
        
        if self.is_empty():
            self.front = node_baru
            self.rear = node_baru
        else:
            self.rear.next = node_baru
            self.rear = node_baru
            
        print(f"Pelanggan {nama} (Antrian {no}) berhasil ditambahkan ke antrian.")

    def dequeue(self):
        # TODO: Layani pelanggan terdepan (Depan/Front)
        if self.is_empty():
            print("Antrian kosong. Tidak ada pelanggan untuk dilayani.")
            return None
            
        # Ambil data pelanggan di depan
        node_dilayani = self.front
        
        # Geser front ke pelanggan berikutnya
        self.front = self.front.next
        
        # Jika antrian jadi kosong, set rear jadi None juga
        if self.front is None:
            self.rear = None
            
        print(f"\n[MEMPROSES] Melayani Pelanggan Antrian No.{node_dilayani.no}")
        print(f"Nama   : {node_dilayani.nama}")
        print(f"Servis : {node_dilayani.servis}")
        return node_dilayani

    def tampilkan(self):
        # TODO: Tampilkan seluruh antrian
        if self.is_empty():
            print("Antrian saat ini KOSONG.")
            return
            
        print("\n=== Daftar Antrian Bengkel Saat Ini ===")
        print(f"{'NO':<5} | {'NAMA PELANGGAN':<20} | {'JENIS SERVIS'}")
        print("-" * 50)
        
        current = self.front
        while current is not None:
            print(f"{current.no:<5} | {current.nama:<20} | {current.servis}")
            current = current.next
        print("-" * 50)


def main():
    q = QueueBengkel()
    
    while True:
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")
        
        pilih = input("Pilih menu: ").strip()
        
        if pilih == "1":
            no = input("No Antrian: ").strip()
            nama = input("Nama: ").strip()
            servis = input("Servis: ").strip()
            
            if not no or not nama or not servis:
                print("Data tidak boleh kosong! Silakan ulangi.")
                continue
                
            q.enqueue(no, nama, servis)
            
        elif pilih == "2":
            q.dequeue()
            
        elif pilih == "3":
            q.tampilkan()
            
        elif pilih == "4":
            print("Sistem dihentikan. Terima kasih.")
            break
            
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()