# ===== LATIHAN 4 =====
# Merge dua Single Linked List

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

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


def merge_lists(list1, list2):
    if not list1.head:
        return list2
    if not list2.head:
        return list1

    temp = list1.head
    while temp.next:
        temp = temp.next

    temp.next = list2.head
    return list1


# ===== MAIN PROGRAM =====
list1 = LinkedList()
list2 = LinkedList()

for i in [1, 3, 5, 7]:
    list1.append(i)

for i in [2, 4, 6, 8]:
    list2.append(i)

print("Linked List 1:")
list1.display()

print("Linked List 2:")
list2.display()

merged = merge_lists(list1, list2)

print("Linked List setelah digabung:")
merged.display()