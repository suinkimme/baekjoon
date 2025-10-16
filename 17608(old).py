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
    highest = S[i] # 높은 수 찾고 높은 수를 업데이트 해두면 그 뒤 숫자를 카운트 안함;; 와 이걸 생각못했네

print(count)