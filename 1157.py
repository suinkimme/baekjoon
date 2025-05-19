s = str(input()).upper()
w = list(set(s))
cnt = []
for i in w:
  cnt.append(s.count(i))

if cnt.count(max(cnt)) > 1:
  print("?")
else:
  print(w[(cnt.index(max(cnt)))])

"""
1. 문자열을 소/대문자로 변경한다.
2. 중복을 허용하지 않는 자료형인 set을 사용한다. (순서도 없다)
3. 입력한 문자열에 중복이 제거된 데이터를 반복하면서 갯수를 알아내 배열에 넣는다.
4. 그 중 가장큰 수를 찾는다.
5. 그 수의 인덱스로 set에서 value를 찾는다.

set된 리스트에 순서대로 값이 삽입될거라 크게 문제 없음
"""