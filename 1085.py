x, y, w, h = map(int, input().split())

l = x
t = h - y
r = w - x
b = y

print(min(l, t, r, b))