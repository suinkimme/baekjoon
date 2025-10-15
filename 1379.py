import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
sch = []
for _ in range(n):
  number, start, end = list(map(int, input().split()))
  sch.append((number, start, end))

sch = sorted(sch, key=lambda x: (x[2], x[1]))

queue = deque([sch[0]])

room = 0
while queue:
  room += 1
  number, start, end = queue.popleft()
  for i in range(n):
    if number == sch[n][0]:
      continue

    if end <= sch[n][1]:
      
    else:
      queue.heappush(sch)