#===================================
# Nama : Misael Christopher Haryanto
# Kelas : TPL P1
#===================================

import time
import random

#===================================
# 1️⃣ Insertion Sort Manual
#===================================

def insertion_sort(data):
    comparisons = 0
    shifts = 0

    for index in range(1, len(data)):
        current_value = data[index]
        position = index

        while position > 0 and data[position - 1] > current_value:
            comparisons += 1
            data[position] = data[position - 1]
            shifts += 1
            position -= 1

        data[position] = current_value

    return data, comparisons, shifts


#===================================
# 2️⃣ TEST DATA
#===================================

data = [54, 26, 93, 17, 77, 31, 44, 55, 20]

print("DATA AWAL :", data)

#===================================
# 3️⃣ Insertion Sort Manual
#===================================

start = time.time()
sorted_manual, comp, shift = insertion_sort(data.copy())
end = time.time()

print("\n=== INSERTION SORT MANUAL ===")
print("Hasil :", sorted_manual)
print("Perbandingan :", comp)
print("Pergeseran :", shift)
print("Waktu Eksekusi :", round(end - start, 6), "detik")


#===================================
# 4️⃣ sorted() (BUILT-IN)
#===================================

start = time.time()
sorted_builtin = sorted(data)
end = time.time()

print("\n=== SORTED() BUILT-IN ===")
print("Hasil :", sorted_builtin)
print("Data asli tetap :", data)
print("Waktu Eksekusi :", round(end - start, 6), "detik")


#===================================
# 5️⃣ sort() METHOD
#===================================

data_sort_method = data.copy()

start = time.time()
data_sort_method.sort()
end = time.time()

print("\n=== LIST.SORT() METHOD ===")
print("Hasil :", data_sort_method)
print("Waktu Eksekusi :", round(end - start, 6), "detik")


#===================================
# 6️⃣ BENCHMARK DATA BESAR
#===================================

print("\n=== BENCHMARK 1000 DATA ===")

data_large = random.sample(range(1, 10000), 1000)

# Insertion Sort
start = time.time()
insertion_sort(data_large.copy())
end = time.time()
print("Insertion Sort :", round(end - start, 6), "detik")

# sorted()
start = time.time()
sorted(data_large)
end = time.time()
print("sorted() :", round(end - start, 6), "detik")

# sort()
data_copy = data_large.copy()
start = time.time()
data_copy.sort()
end = time.time()
print("list.sort() :", round(end - start, 6), "detik")