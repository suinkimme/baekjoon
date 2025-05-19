a, b = list(map(str, input().split()))

a = a[::-1]
b = b[::-1]

if (a * 1) > (b * 1):
  print(a)
else:
  print(b)