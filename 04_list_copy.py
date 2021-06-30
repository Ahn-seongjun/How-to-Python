# 04_list_copy.py

# 리스트 변수 복사

a = [1,2,3]
# 리스트 [1,2,3]을 메모리 어딘가에 저장하고 저장되어있는 주소를 a가 갖고 있다.
# a 리스트의 값을 b 변수에 복사하시오.(저장하시오)
# 얕은 복사 : 원본을 변경하면 같이 변경됨
b=a
# a변수의 값을 b변수에 저장하는 코드(논리적)
print(a)
print(b)

b[0] = 100

print(a)
print(b)
# b[0]원소값을 변경했는데 a[0]의 원소값도 변경
# 둘이 같은 곳에서 온 것이기 때문에 동일하게 변경됨

# 깊은복사(deep copy)
# list() 함수 또는 deepcopy()함수를 사용해서
# 리스트와 복사본을 새로 생성하여 반환
# 복사본 리스트 원소의 값을 변경하여도
# 원본 리스트 원소의 값은 변경되지않음

scores=[1,2,3,4,5]
values = list(scores)
print(scores)
print(values)

values[0]=100
print("scores :",scores)
print("values :",values)

# deepcopy() 함수 : 깊은 복사
# copy 모듈은 import 해야함

import copy

a=['a','b','c']
b=copy.deepcopy(a)

print('b리스트 수정 전')
print(a)
print(b)

b[0]=1

print('b리스트 수정 후')
print(a)
print(b)
