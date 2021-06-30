# 06_list_append_insert.py

# append()
a=[1,2,3,4]
a.append(5) # a 리스트 마지막 요소로 5를 추가하고 a에 저장(원본 변경)
print(a)

a.append([6,7])
print(a)

#a.append(8,9) # 원소를 두 개 추가 - 에러남

# 빈 리스트 생성 후 요소 나중에 추가
values =[]
values.append(10)
values.append(20)
values.append(30) # [10,20,30]
print(values)

# 사용자에게 5개의 값을 입력받아서 리스트에 저장하는 코드
# scores=[]
# for i in range(5):
#     num=int(input('값을 입력하세요: '))
#     scores.append(num)
#     print(i+1,'번째 입력 결과', scores)
# print(scores)
# 위 코드에서 입력받은 값을 각 요소로 출력하는 코드를 작성하시오
# 리스트 요소 출력
# for s in range(len(scores)) :
#     print(s+1, '번째 요소 :', scores[s])

# insert(위치(인덱스 값), 값) : 리스트 특정 위치에 요소 삽입
nums=[1,2,3,4,5]
nums.insert(1,200) # 두번째 위치에 삽입
print(nums)

nums.insert(-1,'홍길동')
print(nums) # 마지막 원소 앞에 삽입

# insert 함수를 이용한 맨 뒤에 삽입
nums.insert(7,12.3)
print(nums)

nums.insert(len(nums)-1,[10,20]) #7번째에 삽입(마지막원소 앞에 삽입)
print(nums)
