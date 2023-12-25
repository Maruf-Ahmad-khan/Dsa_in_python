def binary_search(matrix, rows, cols, key):
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == key:
                return True
    return False

rows = 4
cols = 3
key = 15

# Enter input
print("Enter the input of matrices:\n")
matrix = [[int(input()) for _ in range(cols)] for _ in range(rows)]

# Printing matrix row-wise
print("Printing matrix row-wise:\n")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print()

# Check if the key is present using binary search
print("The key is:", binary_search(matrix, rows, cols, key))
