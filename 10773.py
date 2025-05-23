import sys
input = sys.stdin.readline

K = int(input())
S = []

for _ in range(K):
  a = int(input())
  if a == 0:
    S.pop()
  else:
    S.append(a)

print(sum(S))