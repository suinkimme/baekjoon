import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

"""
1부터 N까지 카드가 쌓여있다. (1이 젤 위, N이 가장 아래)
첫장을 버린다.
다음 장을 N밑에 넣는다.
반복한다.
가장 마지막에 남는 카드 번호를 출력한다.
"""

S = deque(range(1, N + 1))

while len(S) > 1:
  S.popleft()
  S.append(S.popleft())

print(S[0])
