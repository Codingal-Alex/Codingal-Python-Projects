
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


n = int(input("Enter array size: "))

arr = []
print("Enter array elements:")

for i in range(n):
    arr.append(int(input()))

sorted_arr = quick_sort(arr)

print("Sorted array:")
print(*sorted_arr)
