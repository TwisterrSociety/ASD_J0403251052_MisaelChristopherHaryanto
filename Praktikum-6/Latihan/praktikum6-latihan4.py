"""
Nama  : Misael Christopher Haryanto
NIM   : J0403251052
Kelas : TPL B1

Praktikum 6 - Latihan 4
Memahami Merge Sort
"""

def merge_sort(data):

    # Base Case
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


"""
Jawaban:

1. Base case adalah kondisi penghentian rekursi,
   yaitu ketika panjang list <= 1.

2. Fungsi memanggil dirinya sendiri karena
   menggunakan konsep rekursi (divide and conquer).

3. Fungsi merge() bertujuan menggabungkan dua list
   yang sudah terurut menjadi satu list terurut.
"""

# Test
data = [5, 2, 4, 6, 1, 3]
print("Hasil Merge Sort:", merge_sort(data))