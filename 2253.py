"""
돌들이 같은 간격으로 N개 놓여있다.
난 지금 1번 돌 위에 있음
이 돌들 사이에서 점프로 N번째로 가려고한다.
점프하는 조건은 아래와 같다:
  이동은 앞으로만 가능
  점프 이후에 감속, 유지, 가속을 할 수 있음 (감, 가속은 +-1임)
  무조건 1칸은 뛰어야함
각 돌들의 크기는 다르다.
몇 개의 돌은 크기가 너무 작아서 점프할 수 없다.
1번에서 N번까지 점프 해 갈 때 최소 점프 횟수를 구해라
"""

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split()) # 마지막 돌, 못 밟는 돌 개수
B = set(int(input()) for _ in range(M)) # 못 밟는 돌

visited = [set() for _ in range(N + 1)]
queue = deque()
queue.append((1, 0)) # (현재 위치, 이전 점프 거리)

step = 0
while queue:
  step += 1
  for _ in range(len(queue)): # 현재 '단계'에 있는 모든 상태 탐색
    pos, k = queue.popleft() # 큐를 빼서 또 그 다음에 이동할 수 있는지 각을 잰다.

    for nk in [k - 1, k, k + 1]: # 각은 여기서 잼 (세개 다 이동해봄 그러고 안되면 continue 해버림)
      if nk <= 0: # 각 잰 거리가 0보다 작으면 이 거리는 무시함 (대부분 k - 1을 무시하는거임)
        continue
      
      next_pos = pos + nk # pos가 현재 돌이고 nk가 각잰 점프 거리인데 그 값을 더해서 도착할 돌의 index를 유추함
      # 다음 돌의 index가 주어진 N(마지막 돌 index)보다 크면 continue
      # 다음 돌의 index가 못 밟는 돌 set 자료구조에 담겨 있으면 continue
      if next_pos > N or next_pos in B:
        continue

      # 만약에 다음으로 이동하려는 돌에 내가 지금 점프하려는 거리만큼으로 도달한 적이 있으면 continue
      # DP
      if nk in visited[next_pos]:
        continue
      
      # 점프하려는 돌이 마지막돌과 같으면 프로그램 끝내버림
      if next_pos == N:
        print(step)
        exit(0)
      
      # 이걸 다 통과했다면, 그 돌에는 지금 점프거리로 도착한 적이 없다는 거임
      # 그러니까 이제 기록하고
      # 그 다음 돌로 계속 뛰어봄
      visited[next_pos].add(nk) # 이전 점프 거리 기록 (next_pos = 가려는 돌, nk = 가려는 돌에 도달할 수 있는 점프 거리)
      queue.append((next_pos, nk)) # 점프 성공해서 그 값을 큐에 담는다.

# 모든 queue를 탐색했음에도 불구하고 N에 도달하지 못했다면, -1 출력
print(-1)
