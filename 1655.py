# 1 5 2 10 -99
# -99 1 2 5 10

# 1 5 2 10 -99 7 5
# -99 1 2 5 5 7 10 이게 왜 5일까? -> 홀수니까
import heapq
import sys
input = sys.stdin.readline

n = int(input())
left = []
right = []

for _ in range(n):
  x = int(input())

  heapq.heappush(left, -x)

  if right and -left[0] > right[0]:
    val = -heapq.heappop(left)
    heapq.heappush(right, val)
    heapq.heappush(left, -heapq.heappop(right))

  if len(left) > len(right) + 1:
    heapq.heappush(right, -heapq.heappop(left))
  elif len(right) > len(left):
    heapq.heappush(left, -heapq.heappop(right))
  
  print(-left[0])
