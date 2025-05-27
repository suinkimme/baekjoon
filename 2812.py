import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
numbers = input().rstrip()

stack = []
for number in numbers:
  while stack and stack[-1] < number and k > 0:
    stack.pop()
    k -= 1
  stack.append(number)
if k > 0:
  print(''.join(stack[:-k]))
else:
  print(''.join(stack))

"""
1. 입력 받은 숫자를 반복한다.
2. 반복되는 숫자가 스택 top의 숫자보다 크고, 스택에 원소가 존재하고 숫자를 뺄 수 있는 횟수가 남아있다면
    스택 마지막 요소 제거
    숫자를 뺏으니 횟수 차감
3. 해당하지 않는 숫자는 추가
"""