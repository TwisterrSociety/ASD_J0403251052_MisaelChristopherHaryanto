# ===== LATIHAN 1 =====
# Delete node dengan nilai tertentu

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, key):
        temp = self.head

        # jika node yang dihapus adalah head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print(f"Data {key} tidak ditemukan")
            return

        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


# ===== MAIN PROGRAM =====
ll = LinkedList()

for i in [1, 3, 5, 7]:
    ll.append(i)

print("Sebelum dihapus:")
ll.display()

ll.delete_node(5)

print("Setelah dihapus:")
ll.display()# ===== LATIHAN 1 =====
# Delete node dengan nilai tertentu

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, key):
        temp = self.head

        # jika node yang dihapus adalah head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print(f"Data {key} tidak ditemukan")
            return

        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


# ===== MAIN PROGRAM =====
ll = LinkedList()

for i in [1, 3, 5, 7]:
    ll.append(i)

print("Sebelum dihapus:")
ll.display()

ll.delete_node(5)

print("Setelah dihapus:")
ll.display()