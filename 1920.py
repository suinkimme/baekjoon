import sys
input = sys.stdin.readline

N = int(input())
NA = list((map(int, input().split())))

M = int(input())
MA = list((map(int, input().split())))

numbers = set(NA)

for i in MA:
  if i in numbers:
    print(1)
  else:
    print(0)