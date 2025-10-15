N = int(input())
NA = list(map(int, input().split()))
M = int(input())
MA = list(map(int, input().split()))

for i in MA:
  if i in NA:
    print(1)
  else:
    print(0)