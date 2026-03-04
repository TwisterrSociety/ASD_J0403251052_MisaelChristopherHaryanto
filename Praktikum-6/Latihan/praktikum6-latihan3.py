"""
Nama  : Misael Christopher Haryanto
NIM   : J0403251052
Kelas : TPL B1

Praktikum 6 - Latihan 3
Tracing Insertion Sort
"""

def insertion_sort_trace(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        print(f"\nIterasi i = {i}, key = {key}")

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key
        print("List sekarang:", data)

    return data


data = [5, 2, 4, 6, 1, 3]
print("Data awal:", data)
insertion_sort_trace(data)


"""
Jawaban:

1. Setelah i = 1:
   [2, 5, 4, 6, 1, 3]

2. Setelah i = 3:
   [2, 4, 5, 6, 1, 3]

3. Pada iterasi i = 4 (key = 1),
   terjadi 4 kali pergeseran.
"""