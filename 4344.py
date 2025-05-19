c = int(input())

for i in range(c):
  s = list(map(int, input().split()));
  t = sum(s[1:])
  a = t / s[0]
  
  count = 0
  for j in s[1:]:
    if j > a:
      count += 1
  
  r = (count / s[0]) * 100;

  print(f'{r:.3f}%')