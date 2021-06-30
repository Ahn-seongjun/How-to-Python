# 05_list_함수정리.py
# len() : 리스트의 길이 반환
a=[1,2,3,3,4]
print(len(a))
# count() : 리스트 내의 특정 요소의 개수 세기(리스트 객체 메서드)
# 리스트.count(요소)
print(a.count(3))
# append() : 리스트의 끝에 새로운 요소 추가
# 리스트.append(새로 추가할 요소)
# insert() : 리스트의 특정위치에 요소 삽입
# 리스트.insert(삽입위치, 새로 추가할 요소)
# 06_list_append_insert에 정리


# remove() : 리스트에서 값에 해당되는 요소 제거
# 리스트.remove(제거할 요소 값)
# 동일한 값이 여러개 있는 경우 첫 번째 값만 제거
# 동일한 값 모두를 제거하려면 for문 사용

# pop() : 값을 반환하고 삭제
# 리스트.pop()
# 리스트의 마지막 요소 반환하고 삭제
# 리스트.pop(인덱스 값)
# 인덱스 위치에 있는 요소 반환 삭제
# 07_list_remove_pop에 정리

# extend()
# 리스트의 확장
# 리스트.extend()
# 이전 리스트에 원소 추가하여 확장된 리스트로 됨
# 원래 리스트 변경 됨
a=[1,2,3]
a.extend([4,5])
print('a리스트:',a) # 원소 확장되면서 리스트 확장
b=[1,2,3]
b.append([4,5])
print('b리스트:',b) # 하위리스트로 들어감
# extend는 리스트 원소가 추가되면 리스트 확장
# append는 추가된 원소가 리스트면 하위리스트로 추가됨

c=[1,2,3]
c.insert(len(c),[4,5])
print('c리스트:',c) # 하위 리스트로 추가

# sort() / reverse()/sorted() : 원소의 정렬과 관계되는 함수
# 08_list_sort_reverse_sorted에 정리

# index()
# 리스트 안에서 원소의 위치 값 반환
# 리스트.index(값)
a=[1,2,3,4,5,5]
print(a.index(3))
print(a.index(5))
#print(a.index(10)) # 10이라는 원소가 존재하지 않아 에러남

# min() : 리스트 내에서 최소값 원소반환
# max() : 리스트 내에서 최대값 원소반환
n=[100,7,-2,99,30]
char=['c','a','D','A','b']
n_char=[1,300,'a','D',-2]

print(min(n))
print(max(n))

print(min(char))
print(max(char))

# 복합 자료형인 경우 max, min함수 사용불가
#print(min(n_char)) # 에러남
#print(max(n_char)) # 에러남

# in/not in (포함 여부 판단 후 True/False로 반환)
num=[1,2,3,4,5]
result=2 in num # 2가 있니?
print(result) # True

result=2 not in num # 2가 없니?
print(result) # False
print("================")
# 리스트 일치 검사
# 비교 연산자를 사용해서 2개의 리스트 비교('==', '!=', '>=', '<=', '<', '>')
# 첫번째 요소부터 비교 시작
# 첫번째 요소의 비교에서 결과가 False면 더 이상 비교하지 않고 첫번재 요소가 동일하면 두번째 요소 비교.
# 리스트 안의 모든 요소 비교결과가 True 면 전체 결과 : True

list1=[5,2,3]
list2=[1,2,3]

print(list1>=list2)