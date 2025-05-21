n = int(input())

cols = [False] * n
diag1 = [False] * (2 * n - 1)
diag2 = [False] * (2 * n - 1)
count = 0

def nq(row):
  global count
  if row == n:
    count += 1
    return
  
  for col in range(n):
    if cols[col] or diag1[row + col] or diag2[row - col + n - 1]:
      continue
  
    cols[col] = True
    diag1[row + col] = True
    diag2[row - col + n - 1] = True

    nq(row + 1)

    cols[col] = False
    diag1[row + col] = False
    diag2[row - col + n - 1] = False

nq(0)

print(count)

"""
if:
cols[col] => 같은 선상에 퀸이 있는지
diag1[row + col] => 대각선에 퀸이 있는지
diag2[row - col + n - 1] => 대각선에 퀸이 있는지
  빼기를 하면 인덱스가 -가 나올수도 있으니 나지않게 처리
재귀가 끝나면 검사했던 체스판 원상복귀 (다음 케이스를 찾아야하기 때문)
"""