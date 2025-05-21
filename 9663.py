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