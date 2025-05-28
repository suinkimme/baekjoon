import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())
APPLES = set()
for _ in range(K):
  x, y = map(int, input().split())
  APPLES.add((x, y))

L = int(input())
ROTATES = {}
for _ in range(L):
  X, C = input().split()
  ROTATES[int(X)] = C

SNAKE = deque([(1, 1)])
DIRECTION = [(0, 1), (1, 0), (0, -1), (-1, 0)]
DIRECTION_INDEX = 0
SECONDS = 0
while True:
  SECONDS += 1
  HEAD_X, HEAD_Y = SNAKE[0]
  D_X, D_Y = DIRECTION[DIRECTION_INDEX]
  NEW_HEAD = (HEAD_X + D_X, HEAD_Y + D_Y)

  if not (1 <= NEW_HEAD[0] <= N and 1 <= NEW_HEAD[1] <= N):
    break

  if NEW_HEAD in SNAKE:
    break

  SNAKE.appendleft(NEW_HEAD)

  # 사과와 머리 위치를 비교
  # 머리 위치가 사과 배열에 존재하면 사과 삭제
  # 머리 위치가 사과 배열에 존재하지 않으면 뱀.pop()
  if SNAKE[0] in APPLES:
    APPLES.remove(SNAKE[0])
  else:
    SNAKE.pop()

  if SECONDS in ROTATES:
    if ROTATES[SECONDS] == 'D':
      DIRECTION_INDEX = (DIRECTION_INDEX + 1) % 4
    else:
      DIRECTION_INDEX = (DIRECTION_INDEX - 1) % 4

print(SECONDS)
