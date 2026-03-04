"""
Nama  : Misael Christopher Haryanto
NIM   : J0403251052
Kelas : TPL B1

Praktikum 6 - Latihan 5
Melengkapi Fungsi Merge
"""

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        # Kondisi ascending
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # extend() menambahkan sisa elemen
    result.extend(left[i:])
    result.extend(right[j:])

    return result


"""
Jawaban:

1. Kondisi ascending adalah:
   left[i] < right[j]

2. result.extend() berfungsi menambahkan
   seluruh sisa elemen yang belum diproses
   ke dalam list result.
"""

# Test
print(merge([1,4,6], [2,3,5]))