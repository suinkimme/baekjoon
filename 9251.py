import sys
input = sys.stdin.readline

x = list(map(str, input().strip()))
y = list(map(str, input().strip()))

n = len(x)
m = len(y)

memo = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
  for j in range(1, m + 1):
    if x[i - 1] == y[j - 1]:
      memo[i][j] = memo[i - 1][j - 1] + 1
    else:
      memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])

print(memo[n][m])