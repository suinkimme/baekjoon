import sys

input = sys.stdin.readline

n = int(input())

stairs = [0]
for _ in range(n):
  stairs.append(int(input()))

memo = [0] * 301
memo[1] = stairs[1]
memo[2] = stairs[1] + stairs[2]
memo[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, n + 1):
  memo[i] = max(memo[i - 3] + stairs[i - 1] + stairs[i], memo[i - 2] + stairs[i])

print(memo[n])