N, S = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

def d(idx, current):
  global count
  if idx == N:
    if current == S:
      count += 1
    return
  
  d(idx + 1, current + arr[idx])
  d(idx + 1, current)

d(0, 0)
print(count if S != 0 else count - 1)