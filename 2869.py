import math
a, b, v = list(map(int, input().split()))
t = v - b # 총 올라가야하는 높이 (밤에 떨어지는거 예상해서 -b)
o = a - b # 하루에 올라가는 높이
print(math.ceil(t / o))