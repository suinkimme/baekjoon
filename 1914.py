k = int(input())

def hanoi(k, start, end, temp):
  if k == 0:
    return
  hanoi(k - 1, start, temp, end)
  print(start, end)
  hanoi(k - 1, temp, end, start)
  

print(2 ** k - 1)

if k <= 20:
  hanoi(k, 1, 3, 2)