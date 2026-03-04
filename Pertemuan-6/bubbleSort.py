#===================================
# Nama : Misael Christopher Haryanto
# Kelas : TPL P1
#===================================

# Bubble Sort Implementation

import time
import random


#===================================
# Bubble Sort Versi Dasar
#===================================

def bubble_sort_basic(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return arr, comparisons, swaps


#===================================
# Bubble Sort Versi Optimized
#===================================
def bubble_sort_optimized(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True

        if not swapped:
                break
    return arr, comparisons, swaps

#===================================
# Test Case
#===================================

print("=== Test Case ===")
data = [5, 3, 8, 4, 2]
print("Data Awal:", data)

hasil, comp, swap = bubble_sort_basic(data.copy())

print("Hasil Sorting:", hasil)
print("Jumlah Perbandingan:", comp)
print("Jumlah Swap:", swap)

print("\n")

#===================================
# Test Best Case (Sudah Terurut)
#===================================

print("===== TEST BEST CASE =====")
data_best = [1, 2, 3, 4, 5]

hasil, comp, swap = bubble_sort_optimized(data_best.copy())

print("Data:", data_best)
print("Hasil:", hasil)
print("Perbandingan:", comp)
print("Swap:", swap)

print("\n")

#===================================
# Test Worst Case (Terbalik)
#===================================

print("=== WORST CASE===")
data_worst = [5, 4, 3, 2, 1]

hasil, comp, swap = bubble_sort_basic(data_worst.copy())

print("Data:", data_worst)
print("Hasil:", hasil)
print("Perbandingan:", comp)
print("Swap:", swap)

print("\n")

#===================================
# Benchmark Data
#===================================

print("=== BENCHMARK 1000 DATA")

data_large = list(range(1000, 0, -1)) #worst case

start = time.time()
bubble_sort_basic(data_large.copy())
end = time.time()

print("Waktu eksekusi (1000 data - basic):", round(end - start, 5), "detik")

start = time.time()
bubble_sort_optimized(data_large.copy())
end = time.time()

print("Waktu eksekusi (1000 data - optimized):", round(end - start, 5), "detik")

print("\nSelesai.")