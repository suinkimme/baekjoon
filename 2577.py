a = int(input())
b = int(input())
c = int(input())
m = f'{a * b * c}'

d = {
  '0': 0,
  '1': 0,
  '2': 0,
  '3': 0,
  '4': 0,
  '5': 0,
  '6': 0,
  '7': 0,
  '8': 0,
  '9': 0
}

for i in m:
  d[i] += 1

for v in d.values():
  print(v)