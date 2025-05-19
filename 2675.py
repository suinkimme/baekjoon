c = int(input())
for i in range(c):
  s = list(input().split())
  l = int(s[0])
  for j in s[1]:
    print(j * l, end="")
  print()