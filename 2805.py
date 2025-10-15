# 니무 배열이 주어짐
# 절단기 높이를 맞춤
# 내가 갖고 싶은 미터를 최소한으로 넘는 나무 길이를 얻을 수 있는 절단기 높이는 얻어야함

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

r = max(trees)
l = 0
h = 0

# r이 줄어들다보면 l과 만나서 언젠간 멈춤
while l <= r:
  # 중간값을 구함
  mid = r + l // 2
  # 자른 나무들의 총 길이
  t = 0
  for tree in trees:
    # 중간 값 보다 크면 자름
    if tree > mid:
      t += (tree - mid)
  
  # 자른 나무 길이가 목표했던 길이보다 크다면
  if t >= M:
    # 일단 h에 저장 이정도 가져가면 해결되긴 됨
    h = mid
    # 그리고 절단기 높이 하나 더 올려서 확인해봄
    l = mid + 1
  else:
    # 자른 나무 길이가 부족할 경우니까 절단기를 내려서 한번 더 시도
    r = mid - 1
  
print(h)