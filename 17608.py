import sys
input = sys.stdin.readline

S = []
N = int(input())
for _ in range(N):
  h = int(input())
  S.append(h)

S.reverse()
count = 1
highest = S[0]
for i in range(1, len(S)):
  if S[i] > highest:
    count += 1
    highest = S[i]

print(count)