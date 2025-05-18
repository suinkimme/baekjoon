a = (0, 0)
for i in range(9):
  n = int(input())
  if n > a[0]:
    a = (n, i + 1)

print(a[0], a[1], sep='\n')