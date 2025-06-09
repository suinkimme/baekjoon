"""
가볍고 가치가 높은걸 넣는게 맞다.
"""
import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
stuffs = []
for _ in range(n):
  w, v = list(map(int, input().split()))
  stuffs.append((w, v))

memo = [0] * (k + 1)
for w, v in stuffs:
  for j in range(k, w - 1, -1):
     memo[j] = max(memo[j], memo[j - w] + v)

print(memo[-1])