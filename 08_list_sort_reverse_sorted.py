# 08_list_sort_reverse_sorted.py

# sort(): 리스트 정렬, 원본 리스트 변경
scores = [90,78,81,64,89] ;print()
scores.sort() # 오름차순 정렬
print(scores)

scores = [90,78,81,64,89] ;print()
scores.sort(reverse=True) # 내림차순 정렬
print(scores)

scores = [90,78,81,64,89] ;print()
scores.reverse() # 원소 위치 역순 정렬
print(scores)

## 문자의 정렬
char=['b','A','d','C']
char.sort()
print(char)

# 대소문자 구별없이 정렬
# key =str.lower
char=['b','A','d','C']
char.sort(key=str.lower)
print(char)

# 대소문자 구별없이 내림차순 정렬
char=['b','A','d','C']
char.sort(key=str.lower,reverse=True)
print(char)

# 문자열은 첫 문자로 정렬됨
ids=['SKY','Blue','red','eBook','GREEN']
ids.sort() # 오른차순 정렬-첫 문자로 정렬
print(ids)

# 대소문자 구별없이 정렬
ids=['SKY','Blue','red','eBook','GREEN']
ids.sort(key=str.lower) # 오른차순 정렬-첫 문자로 정렬
print(ids)

# sorted() : 원본 유지하면서 정렬된 새로운 리스트 반환
a=[3,5,2,1,4]
b=sorted(a)
print('a',a)
print('b',b)