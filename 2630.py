import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
white = 0
blue = 0

def cut(row, column, n):
  # 함수 안에서 글로벌에 있는 변수를 사용하게 해줌
  global white, blue
  # 처음 찾을 색
  color = paper[row][column]
  for i in range(row, row + n):
    for j in range(column, column + n):
      # 찾아가 처음 지정한 색이랑 내가 지금 찾고있는 영역안에서 색이 다르다? 그러면 그 조각된 것을 또 4등분해서 또 찾음
      if (color != paper[i][j]):
        cut(row, column, n // 2) # 0, 0, 4
        cut(row, column + n // 2, n // 2) # 0, 2, 2
        cut(row + n // 2, column, n // 2) # 2, 0, 2
        cut(row + n // 2, column + n // 2, n // 2) # 2, 2, 2
        return
  
  if color == 0:
    white += 1
  else:
    blue += 1

cut(0, 0, n)
print(white)
print(blue)
