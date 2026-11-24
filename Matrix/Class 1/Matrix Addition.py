# initializing matrices

x = [[3.1, 2,1],
[4, 10, 2]]

y = [[1,2, 3],
[1, 3, 4]]

answer = [[1,0, 5],
[0,0,6]]

for i in range(len(x)):
    for j in range(len(x[0])):
        answer[i][j] =x[i][j] +y[i][j]
for r in answer:
    print(r)
