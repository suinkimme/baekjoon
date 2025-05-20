def h(n):
  count = 0
  for i in range(1, n + 1):
    s = list(map(int, str(i)))
    if i < 100:
      count += 1
    elif s[0] - s[1] == s[1] - s[2]:
      count += 1
  return count

x = int(input())
print(h(x))

"""
1. 100이하의 수는 모두 한수다.
2. 1000은 한수가 아니다.
3. 세자리만 신경쓰면 된다.
4. 123 -> 1 - 2 == 2 - 3을 비교해서 풀었다.
"""