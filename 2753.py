def isLeapYear(year):
  if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    return 1
  return 0

print(isLeapYear(int(input())))