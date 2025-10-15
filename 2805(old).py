"""
나무 M 미터가 필요함
나무를 자르기 위한 절단기 높이 H를 지정해야함
  연속해 있는 나무가 싹- 잘림
  H 위 부분만 잘림
필요한 나무 M 미터 보다 많이 자르면됨 (최소한으로 잘라야함)
"""
import bisect
import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
trees = list(map(int, input().split()))

trees.sort()
l = 0
r = trees[-1]
h = 0

i = bisect.bisect_left(trees, (l + r) // 2)
while l <= r:
  m = (l + r) // 2
  t = 0

  for tree in trees[i:]:
    if tree > m:
      t += (tree - m)
  
  if t >= M:
    h = m
    l = m + 1
  else:
    r = m - 1

print(h)