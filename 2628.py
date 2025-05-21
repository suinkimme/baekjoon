x, y = list(map(int, input().split()))
c = int(input())

w = [0, x]
h = [0, y]

for i in range(c):
  a, p = list(map(int, input().split()))
  if a == 0:
    h.append(p)
  if a == 1:
    w.append(p)

w.sort()
h.sort()

mw = []
mh = []

for i in range(0, len(w) - 1):
  mw.append(abs(w[i] - w[i + 1]))

for i in range(0, len(h) - 1):
  mh.append(abs(h[i] - h[i + 1]))

print(max(mw) * max(mh))