# Take array size from the user
n = int(input())

# Take array elements from the user
arr = list(map(int, input().split()))

# Shell Sort
gap = n // 2

while gap > 0:
    for i in range(gap, n):
        temp = arr[i]
        j = i

        while j >= gap and arr[j - gap] > temp:
            arr[j] = arr[j - gap]
            j -= gap

        arr[j] = temp

    gap //= 2

# Print the sorted array
print(*arr)
