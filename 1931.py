import sys
input = sys.stdin.readline

n = int(input())
m = []
for _ in range(n):
  s, e = list(map(int, input().split()))
  m.append((s, e))

m = sorted(m, key=lambda x: (x[1], x[0]))
pm = [m[0]]
for i in range(1, n):
  if pm[-1][1] <= m[i][0]:
    pm.append(m[i])

print(len(pm))