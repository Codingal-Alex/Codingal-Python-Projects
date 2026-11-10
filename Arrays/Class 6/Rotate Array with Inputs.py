
# Rotate Array with Inputs

# Get the array size
n = int(input("Enter the array size: "))

# Create an empty array
array = []

# Get the array elements
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)

# Rotate one position to the left
rotation1 = array[1:] + array[:1]

# Rotate two positions to the left
rotation2 = array[2:] + array[:2]

# Display the results
print("Original array:", array)
print("Array rotated one position to the left:", rotation1)
print("Array rotated two positions to the left:", rotation2)
