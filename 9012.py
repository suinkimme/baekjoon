import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  V = str(input()).strip()
  while T:
    V = V.replace('()', '')
    if len(V) == 0:
      print('YES')
      break;
    elif '()' not in V and len(V) > 0:
      print('NO')
      break;