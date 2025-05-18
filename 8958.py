n = int(input())

for i in range(n):
  s = [len(v) for v in list(input().split('X')) if v]
  r = 0
  for j in s:
    r += sum(range(1, j + 1))
  print(r)

"""
n = int(input())
for i in range(0,n):
    count, c = 0, 1
    s = list(input())
    for j in s:
        if j == 'O':
            count += c
            c += 1
        else:
            c = 1
    print(count)
"""