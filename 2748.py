import sys
input = sys.stdin.readline

memo = [None] * 91
memo[0] = 0

n = int(input())

for i in range(1, n + 1):
  if i == 1 or i == 2:
    memo[i] = 1
  else:
    memo[i] = memo[i - 1] + memo[i - 2]

print(memo[n])