import sys
input = sys.stdin.readline

n = int(input())
solutions = list(map(int, input().split()))
solutions.sort()

pl = 0
pr = n - 1

answer = abs(solutions[pl] + solutions[pr])
final = (solutions[pl], solutions[pr])

while pl < pr:
  pl_value = solutions[pl]
  pr_value = solutions[pr]

  total = pl_value + pr_value

  if abs(total) < answer:
    answer = abs(total)
    final = (pl_value, pr_value)
    if answer == 0:
      break
  
  if total < 0:
    pl += 1
  else:
    pr -= 1

print(final[0], final[1])