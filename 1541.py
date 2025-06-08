import sys
input = sys.stdin.readline

formula = list(map(str, input().strip().split('-')))

for i in range(len(formula)):
  if '+' in formula[i]:
    formula[i] = sum([int(n) for n in formula[i].split('+')])
  else:
    formula[i] = int(formula[i])

result = formula[0]
for i in range(1, len(formula)):
  result -= formula[i]

print(result)