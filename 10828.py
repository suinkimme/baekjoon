import sys
input = sys.stdin.readline
N = int(input())

S = []
for _ in range(N):
  C = list(map(str, input().split()))
  if C[0] == 'push':
    S.append(C[1])
  elif C[0] == 'pop':
    if len(S) > 0:
      p = S.pop()
      print(p)
    else:
      print(-1)
  elif C[0] == 'size':
    print(len(S))
  elif C[0] == 'empty':
    print(0 if len(S) else 1)
  else:
    print(S[len(S) - 1] if len(S) > 0 else -1)