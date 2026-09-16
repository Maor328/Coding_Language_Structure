
import sys
import time

# Function without Lazy Evaluation (lists)
def measure_non_lazy():
    start = time.perf_counter()
    arr = list(range(10001))
    end = time.perf_counter()
    print(f"Non-Lazy Array Size: {sys.getsizeof(arr)} bytes, Time: {end - start:.6f} s")
    return arr

# Function with Lazy Evaluation (range objects)
def measure_lazy():
    start = time.perf_counter()
    arr = range(10001)
    end = time.perf_counter()
    print(f"Lazy Array Size: {sys.getsizeof(arr)} bytes, Time: {end - start:.6f} s")
    return arr

def measure_sub_non_lazy(arr):
    start = time.perf_counter()
    sub_arr = arr[:5000]
    end = time.perf_counter()
    print(f"Non-Lazy Sub-Array Size: {sys.getsizeof(sub_arr)} bytes, Time: {end - start:.6f} s")
    print(f"Type: {type(sub_arr)}\n")

def measure_sub_lazy(arr):
    start = time.perf_counter()
    # Slicing a range object returns another lazy range object
    sub_arr = arr[:5000] 
    end = time.perf_counter()
    print(f"Lazy Sub-Array Size: {sys.getsizeof(sub_arr)} bytes, Time: {end - start:.6f} s")
    print(f"Type: {type(sub_arr)}\n")

print("--- Testing Phase A & B ---")
arr_non_lazy = measure_non_lazy()
arr_lazy = measure_lazy()

measure_sub_non_lazy(arr_non_lazy)
measure_sub_lazy(arr_lazy)