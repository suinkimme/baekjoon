import sys
input = sys.stdin.readline

s1 = str(input())
s2 = str(input())

n = len(s1)
m = len(s2)

memo = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, n + 1):
  for j in range(1, m + 1):
    if s1[i - 1] == s2[j - 1]:
      memo[i][j] = memo[i - 1][j - 1] + 1
    else:
      memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])
      

print(memo[i][j])