import random

def stand(num):
    global i
    z = []
    for i in num:
        print(i)


num_1 = int(input())
num_2 = int(input())

matrix_1 = []
matrix_2 = []
res = []


for i in range(num_1):
    matrix_zero = []
    for v in range(num_2):
        matrix_zero.append(random.randint(-1000,1000))
    matrix_1.append(matrix_zero)


for i in range(num_1):
    matrix_zero = []
    for v in range(num_2):
        matrix_zero.append(random.randint(-1000,1000))
    matrix_2.append(matrix_zero)


for i in range(len(matrix_1)):
    pre_res = []
    for v in range(len(matrix_1[0 + 1])):
        pre_res.append(matrix_1[i][v] + matrix_2[i][v])
    res.append(pre_res)


stand(matrix_1)
print('\n')
stand(matrix_2)
print('\n')
stand(res)

#Matrix sum and generate