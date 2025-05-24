import sys
input = sys.stdin.readline

N, C = list(map(int, input().split()))

houses = []
for _ in range(N):
  X = int(input())
  houses.append(X)

houses.sort()
left = 1
right = houses[-1] - houses[0]
result = 0

def can_install_with_distance(dist):
  count = 1
  last = houses[0]
  for i in range(1, N):
    if houses[i] - last >= dist:
      count += 1
      last = houses[i]
  return count >= C

while left <= right:
  mid = (left + right) // 2
  if can_install_with_distance(mid):
    result = mid
    left = mid + 1
  else:
    right = mid - 1

print(result)