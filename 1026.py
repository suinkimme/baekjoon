import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0
while B:
  minA = min(A)
  maxB = max(B)
  result += minA * maxB
  A.remove(minA)
  B.remove(maxB)

print(result)