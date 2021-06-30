# 07_list_remove_pop.py
n=[1,2,3,3,4,5,4,3]
n.remove(4) # 4를 제거하고 원본 반영됨
print(n)

# n 리스트에서 원소값이 3인 원소를 모두 제거하시오
# 3의 개수를 확인해야함
count = n.count(3)
for i in range(count):
    n.remove(3)
    print("3 삭제 ", n)

print(n)

n1 =[1,1,2,1]
n1.remove(1)
n1.remove(1)
n1.remove(1)
#n1.remove(1) # 제거할 요소가 없어 에러남

# pop() : 리스트 마지막 요소 반환하고 삭제
x=['a','b','c','d']
y=x.pop() #d
print(y) # 반환된 마지막요소 d
print(x) # d삭제된 나머지 요소만 확인

# x에 남아 있는 요소 3개를 pop
x.pop() #['a','b']
x.pop() #['a']
x.pop() #[]
print(x)

# x가 빈 리스트인 경우 pop() - 에러남

# pop(인덱스) : 인덱스 위치에 있는 요소 반환 삭제
heroes =['슈퍼맨','스파이더맨','헐크','아이언맨','베트맨']
tmp = heroes.pop(2)
print('삭제된 값: ',tmp)
print('삭제 후 리스트', heroes)