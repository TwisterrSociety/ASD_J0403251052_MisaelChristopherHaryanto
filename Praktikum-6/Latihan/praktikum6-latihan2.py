"""
Nama  : Misael Christopher Haryanto
NIM   : J0403251052
Kelas : TPL B1

Praktikum 6 - Latihan 2
Melengkapi Potongan Kode Insertion Sort
"""

def insertion_sort_ascending(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        # Kondisi ascending (kecil ke besar)
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data


def insertion_sort_descending(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        # Kondisi descending (besar ke kecil)
        while j >= 0 and data[j] < key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data


"""
Jawaban:
1. Kondisi ascending adalah: data[j] > key
2. Untuk descending diganti menjadi: data[j] < key
"""

# Test
data = [5, 2, 4, 6, 1, 3]
print("Ascending :", insertion_sort_ascending(data.copy()))
print("Descending:", insertion_sort_descending(data.copy()))