# 나무 M미터가 필요함
# 절단기의 높이 H를 지정한다.
# H보다 큰 나무는 H위의 부분이 잘린다.
# 낮은 나무는 잘리지 않는다.
# 20 15 10 17의 나무가 있으면 절단기 높이를 15로 지정했을 때 5와 2의 나무 두개를 가져갈 수 있다.
# 적어도 M미터의 나무를 집에 가져가기 위한 절단기의 최대값을 구해라
import bisect
import sys
input = sys.stdin.readline

# N 나무의 수
# M 필요한 나무 길이
N, M = map(int, input().split())

# T 나무 배열
T = list(map(int, input().split()))
T.sort()
r = max(T)

l = 0
h = 0
i = bisect.bisect_left(T, ((l + r) // 2))
while l <= r:
  m = (l + r) // 2
  t = 0

  for tree in T[i:]:
    if tree > m:
      t += (tree - m)
  
  if t >= M:
    h = m
    l = m + 1
  else:
    r = m - 1

print(h)
