import sys
inpurt = sys.stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())
  coins = list(map(int, input().split()))
  M = int(input())

  memo = [0] * (M + 1)
  memo[0] = 1
  for coin in coins:
    for i in range(1, M + 1):
      if i >= coin:
        memo[i] += memo[i - coin]
  print(memo[M])