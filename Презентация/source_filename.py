# считываем массив с клавиатуры
A = list(map(int, input().split())
mx = A[0]
i_mx = A[0]
for i in range(1, len(A)):
    if A[i] > mx:
        mx = A[i]
        i_mx = i