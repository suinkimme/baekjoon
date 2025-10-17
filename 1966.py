from collections import deque

T = int(input())

for _ in range(T):
  N, M = map(int, input().split())
  queue = deque(map(int, input().split()))
  idx = deque(range(N))

  count = 0

  while queue:
    if queue[0] == max(queue):
      count += 1
      queue.popleft()
      pos = idx.popleft()
      if pos == M:
        print(count)
        break
    else:
      queue.append(queue.popleft())
      idx.append(idx.popleft())