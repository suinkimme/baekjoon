c = int(input())
n = list(map(int, input().split()))

def isPrime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

cnt = 0
for i in n:
  if isPrime(i) and i > 1:
    cnt += 1

print(cnt)