
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Select the last element as pivot
    pivot = arr[-1]

    # Divide elements into two lists
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    # Recursively sort both lists
    return quick_sort(left) + [pivot] + quick_sort(right)


# Input array
arr = [10, 7, 8, 9, 1, 5]

# Sort the array
sorted_arr = quick_sort(arr)

print("Sorted array:", sorted_arr)
