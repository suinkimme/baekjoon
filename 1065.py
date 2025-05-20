def h(n):
  count = 0
  for i in range(1, n + 1):
    s = list(map(int, str(i)))
    if i < 100:
      count += 1
    elif s[0] - s[1] == s[1] - s[2]:
      count += 1
  return count

x = int(input())
print(h(x))