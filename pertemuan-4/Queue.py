# 1. Kita harus mendefinisikan Class Node terlebih dahulu
class Node:
    def __init__(self, data):
        self.data = data       # Menyimpan data
        self.next = None       # Pointer ke node berikutnya

# 2. Implementasi Queue dengan Front dan Rear
class QueueLL:
    def __init__(self):
        self.front = None      # Node paling depan
        self.rear = None       # Node paling belakang
        
    def enqueue(self, data):
        nodeBaru = Node(data)  # Buat node baru
        
        # PERBAIKAN: Cek apakah queue kosong dengan melihat front
        if self.front is None: 
            self.front = nodeBaru
            self.rear = nodeBaru
            return # Keluar dari fungsi karena tugas sudah selesai

        # Jika queue tidak kosong:
        self.rear.next = nodeBaru # Sambungkan node terakhir saat ini ke node baru
        self.rear = nodeBaru      # Pindahkan label 'rear' ke node baru
        
    def dequeue(self):
        if self.front is None: # Cek apakah queue kosong
            print("Queue kosong, tidak ada yang bisa didequeue")
            return None
        
        data_terdequeue = self.front.data # Simpan data yang akan dikeluarkan
        self.front = self.front.next       # Geser front ke node berikutnya
        
        # Jika setelah dequeue queue menjadi kosong, pastikan rear juga di-reset
        if self.front is None:
            self.rear = None
        
        return data_terdequeue

    def tampilkan(self):
        current = self.front
        print("Isi Queue saat ini: ", end="")
        while current is not None:
            print(f"[{current.data}]", end=" -> ")
            current = current.next
        print("None") # Penanda akhir

# --- Bagian Main Program ---

# Instansiasi objek class QueueLL
q = QueueLL() 

q.enqueue("A") 
q.enqueue("B") 
q.enqueue("C") 

print("Setelah enqueue A, B, C:")
q.tampilkan()