# Leer dimensiones
r, c = map(int, input().split())

# Leer matriz A
A = [list(map(int, input().split())) for _ in range(r)]

# Leer matriz B
B = [list(map(int, input().split())) for _ in range(r)]

# Restar y mostrar resultado
for i in range(r):
    for j in range(c):
        print(A[i][j] - B[i][j], end=" ")
    print()
