N, M = map(int, input().split())
T = list(map(int, input().split()))
H = 0

low = 0
high = max(T)

while low <= high:
  mid = (low + high) // 2
  wood = 0

  for tree in T:
    if tree > mid:
      wood += tree - mid

  if wood >= M:
    H = mid
    low = mid + 1
  else:
    high = mid - 1

print(H)