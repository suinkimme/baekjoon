import sys
from collections import deque

input = sys.stdin.readline

S = deque([])
N = int(input())
for _ in range(N):
  C = list(map(str, input().split()))
  if C[0] == 'push':
    S.append(C[1])
  elif C[0] == 'pop':
    if S:
      print(S.popleft())
    else:
      print(-1)
  elif C[0] == 'size':
    print(len(S))
  elif C[0] == 'empty':
    if len(S) < 1:
      print(1)
    else:
      print(0)
  elif C[0] == 'front':
    if S:
      print(S[0])
    else:
      print(-1)
  else:
    if S:
      print(S[-1])
    else:
      print(-1)