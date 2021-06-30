# 01_list.py

# 리스트 만들기
# 변수명 = [값1, 값2...]

# 단일 자료형
ints = [1, 2, 3, 4, 5]
floats = [1.1, 2.2, 3.3, 4.4, 5.5]
names = ['홍길동', '이몽룡', '성춘향']

# 복합자료형
mix = [1, 5.0, '김철수']

# 리스트 안에 리스트를 포함할 수 있음
numbers = [100, 200, 300, [10,20,30]]

# 리스트 반환
# 리스트 명으로 접근
print(ints)
print(floats)
print(names)
print(numbers)

# 각 원소 접근
for name in names:
    print(name)
    print(type(name))

# 각 원소를 인덱스를 통해 접근 - 원소값 확인
for i in range(0, len(ints)):
    print(ints[i])

# 인덱스를 통해 원소에 접근
print(numbers[3])

# 리스트 각각의 값을 변수에 저장
nums = [1,2,3]
# 리스트 nums의 원소값 각각을 a, b, c변수에 저장 하시오
a=nums[0]
b=nums[1]
c=nums[2]

a,b,c = nums # 리스트 각각의 값을차례대로 앞의 변수에 저장

# 리스트 특징
nums1 = [10, 20, 30]
#a1,b1 = nums1 # 이렇게하면 에러남 ->변수 갯수에 맞게 있어야함
# 왼쪽변수의 개수가 오른쪽 리스트 원소의 개수보다 적으면 안됨

# a1,b1,c1,d1 = nums1 # 왼족 변수의 개수가 오른쪽 리스트 원소 개수보다 많아도 안됨
# print(a1,b1,c1,d1)
