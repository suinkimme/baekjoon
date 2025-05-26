import heapq
import sys
input = sys.stdin.readline

N = int(input())
cards = []
for _ in range(N):
  C = int(input())
  cards.append(C)

heapq.heapify(cards)
answer = 0
while len(cards) > 1:
  first = heapq.heappop(cards)
  second = heapq.heappop(cards)
  answer += first + second
  heapq.heappush(cards, first + second)

print(answer)