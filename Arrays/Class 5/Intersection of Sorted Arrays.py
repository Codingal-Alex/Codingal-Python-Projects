
# Take input for the first array
n1 = int(input("Enter size of first array: "))
arr1 = list(map(int, input("Enter first array elements: ").split()))

# Take input for the second array
n2 = int(input("Enter size of second array: "))
arr2 = list(map(int, input("Enter second array elements: ").split()))

# Find intersection
i = 0
j = 0
result = []

while i < n1 and j < n2:
    if arr1[i] == arr2[j]:
        if not result or result[-1] != arr1[i]:
            result.append(arr1[i])
        i += 1
        j += 1

    elif arr1[i] < arr2[j]:
        i += 1

    else:
        j += 1

# Print the common elements
print("Intersection of arrays:", *result)
