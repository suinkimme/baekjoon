a = int(input())
b = int(input())

c = int(b / 100)
d = int((b - c * 100) / 10)
e = int(b - (c * 100 + d * 10))

print(a * e)
print(a * d)
print(a * c)
print(a * b)

"""
a = int(input())
b = input()

a1 = a * int(b[2])
a2 = a * int(b[1])
a3 = a * int(b[0])
a4 = a * int(b)

print (a1, a2, a3, a4, sep='\n')
"""