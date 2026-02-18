# ==========================================
# 1. Implementasi Dasar: Node Manual
# ==========================================

# Membuat class Node
class Node:
    def __init__(self, data):
        self.data = data       # menyimpan data
        self.next = None       # pointer ke node berikutnya

print("--- DEMO 1: Manual Node Linking ---")

# Membuat node satu per satu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# Menghubungkan node-node tersebut
nodeA.next = nodeB  # nodeA menunjuk ke nodeB
nodeB.next = nodeC  # nodeB menunjuk ke nodeC

# Menentukan node head
head = nodeA 

# Traversing (menelusuri) linked list manual
print("Isi Linked List Manual:")
current = head
while current is not None:
    print(current.data)       # tampilkan data
    current = current.next    # pindah ke node berikutnya

# Menampilkan akses pointer manual
print("\nAkses via pointer:")
print(nodeA.data)             # output: A
print(nodeA.next.data)        # output: B
print(nodeA.next.next.data)   # output: C


# ==========================================
# 2. Implementasi Class Linked List (Insert & Delete)
# ==========================================

class LinkedList:
    def __init__(self):
        self.head = None # Inisialisasi head kosong saat list dibuat

    def insert_awal(self, data):
        new_node = Node(data)       # Buat node baru
        new_node.next = self.head   # Node baru menunjuk ke head lama
        self.head = new_node        # Head diperbarui ke node baru
    
    def hapus_awal(self):
        if self.head is None:       # Cek jika list kosong
            print("List kosong, tidak ada yang dihapus")
            return None
            
        data_terhapus = self.head.data # Simpan data info
        self.head = self.head.next     # Geser head ke node berikutnya
        return data_terhapus

    def tampilkan(self):
        current = self.head
        print("Isi Linked List saat ini: ", end="")
        while current is not None:
            print(f"[{current.data}]", end=" -> ")
            current = current.next
        print("None") # Penanda akhir list

# --- Menjalankan Kode ---
print("\n--- DEMO 2: Class LinkedList ---")

ll = LinkedList()   # Membuat linked list baru

ll.insert_awal("X") # List: X -> None
ll.insert_awal("Y") # List: Y -> X -> None
ll.insert_awal("Z") # List: Z -> Y -> X -> None

print("Setelah insert Z, Y, X:")
ll.tampilkan()      # Menampilkan isi linked list

print("\nMenghapus elemen awal...")
ll.hapus_awal()     # Menghapus "Z"

print("Setelah penghapusan:")
ll.tampilkan()      # Menampilkan sisa linked list (Y -> X)