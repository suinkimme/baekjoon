a = (0, 0)
for i in range(9):
  n = int(input())
  if n > a[0]:
    a = (n, i + 1)

print(a[0], a[1], sep='\n')

"""
numbers = [int(input()) for _ in range(9)]

print(max(numbers)) # 가장 큰 값 출력
print(numbers.index(max(numbers)) + 1) # 값으로 인덱스를 찾는건데 같은 값이 있으면 어떻게 처리하지? -> 처음 값을 반환함
"""