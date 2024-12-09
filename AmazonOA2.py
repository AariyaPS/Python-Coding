from collections import Counter
 
def min_operations_to_destroy_array(arr):
    freq_map = Counter(arr)
 
    min_operations = 0
    for freq in freq_map.values():
        if freq == 1:
            return -1  # According to Tariquddin’s law
        else:
            # According to Tanmai’s Law
            min_operations += freq // 3 + (1 if freq % 3 != 0 else 0)
    return min_operations
 
arr = [1, 5, 5, 1, 1, 8, 8, 10, 10]
min_ops = min_operations_to_destroy_array(arr)
if min_ops == -1:
    print("It's not possible to destroy the array.")
else:
    print("Minimum number of operations to destroy the array:", min_ops)

