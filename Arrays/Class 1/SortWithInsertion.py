# Take array size from the user
n = int(input())

# Take array elements from the user
arr = list(map(int, input().split()))

# Insertion Sort
for i in range(1, n):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

# Print the sorted array
print(*arr)
