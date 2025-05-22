T = int(input())
A = [0] * 12

A[1] = 1 # 1
A[2] = 2 # 1 + 1, 2
A[3] = 4 # 1 + 1 + 1, 1 + 2, 2 + 1, 3

for i in range(4, 12):
  A[i] = A[i - 1] + A[i - 2] + A[i - 3]

for _ in range(T):
  n = int(input())
  print(A[n])