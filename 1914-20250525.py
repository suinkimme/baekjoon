"""
3개의 장대가 있다. (고정)
ㅗ ㅗ ㅗ <- 이런식
1. 한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
2. 쌓아 놓은 원판은 항상 위의 것이 라애의 것보다 작아야 한다.
"""

import sys
input = sys.stdin.readline
n = int(input())
def hanoi(n, start, end, temp):
  if n == 0:
    return
  hanoi(n - 1, start, temp, end)
  print(start, end)
  hanoi(n - 1, temp, end, start)

print(2 ** n - 1)

if n <= 20:
  hanoi(n, 1, 3, 2)
