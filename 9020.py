c = int(input())

def is_prime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

for i in range(0, c):
  n = int(input())
  h = n // 2
  if is_prime(h):
    print(f'{h} {h}')
  else:
    k = h
    for j in range(h, n):
      k -= 1
      if is_prime(n - k) and is_prime(k):
        print(f'{k} {n - k}')
        break;