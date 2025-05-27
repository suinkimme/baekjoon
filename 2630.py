import sys

input = sys.stdin.readline
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
white = 0
blue = 0

def cut(row, column, n):
  global white, blue
  color = paper[row][column]
  for i in range(row, row + n):
    for j in range(column, column + n):
      if color != paper[i][j]:
        cut(row, column, n // 2) # 0 0 4
        cut(row, column + n // 2, n // 2) # 0 4 4
        cut(row + n // 2, column, n // 2) # 4 0 4
        cut(row + n // 2, column + n // 2, n // 2) # 4 4 4
        return
  if color == 0:
    white += 1
  else:
    blue += 1

cut(0, 0, n)
print(white)
print(blue)

"""
[
  [1, 1, 0, 0, 0, 0, 1, 1],
  [1, 1, 0, 0, 0, 0, 1, 1],
  [0, 0, 0, 0, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 1, 0, 0],
  [1, 0, 0, 0, 1, 1, 1, 1],
  [0, 1, 0, 0, 1, 1, 1, 1],
  [0, 0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 1, 1, 1, 1, 1]
]

1. 가장 왼쪽 위의 색과 size별로 반복하며 한 칸 한 칸 검사를 한다.
2. 색이 다르면 함수를 중단하고 size를 // 2해서 반으로 쪼개 다시 검사를 한다.
3. 이걸 반복한다.
4. 가장 왼쪽 위와 색이 같다면 이중포문이 끝나고 색에 맞게 카운트가 추가된다.
"""