N = int(input())
origin = N
count = 0

while True:
  a = N // 10
  b = N % 10
  c = (a + b) % 10
  N = b * 10 + c
  count += 1
  if N == origin:
    break

print(count)