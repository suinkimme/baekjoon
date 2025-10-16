import sys
input = sys.stdin.readline

n = int(input())
sticks = []
for i in range(n):
  sticks.append(int(input()))

count = 1
sticks.reverse()
last = sticks[0]
for i in sticks[1:]:
  if last < i:
    count += 1
    last = i

print(count)