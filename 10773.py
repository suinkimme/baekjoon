import sys
input = sys.stdin.readline

k = int(input())
total = []
for i in range(k):
  n = int(input())
  if n == 0:
    total.pop()
  else:
    total.append(n)

print(sum(total))