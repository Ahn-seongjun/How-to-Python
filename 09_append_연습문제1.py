# 09_append_연습문제1.py

names=[]
for i in range(5):
     name=input('회원 입력 : ')
     names.append(name)

print('회원 명단 :',end='')
for name in names:
     print(name, end=' ')