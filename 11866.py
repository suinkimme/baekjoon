import sys
from collections import deque
input = sys.stdin.readline

N, K = list(map(int, input().split()))
Q = deque(range(1, N + 1))
NQ = []

while N > len(NQ):
  Q.rotate((K - 1) * -1)
  NQ.append(Q.popleft())

print("<" + str(NQ)[1: len(str(NQ)) - 1] + ">")