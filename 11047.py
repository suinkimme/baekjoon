import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
m = []
for _ in range(n):
  a = int(input())
  if a <= k:
    m.append(a)

count = 0
for a in range(len(m) - 1, -1, -1):
  if m[a] > k:
    continue

  count += k // m[a]
  k = k % m[a]

  if k == 0:
    break

print(count)