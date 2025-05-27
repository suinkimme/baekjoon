import sys
import heapq
input = sys.stdin.readline
n = int(input())

queue = []
for _ in range(n):
  x = int(input())
  if x != 0:
    heapq.heappush(queue, x * -1)
  else:
    if len(queue) > 0:
      print(heapq.heappop(queue) * -1)
    else:
      print(0)