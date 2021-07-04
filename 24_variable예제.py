# 24_variable예제.py

def sub(x,y):
    global a

    a=7 # 전역변수 a를 7로 변경
    x,y = y,x # 지역변수 지정
    b=3 # 지역변수 지정
    print(a,b,x,y) # 7243

a,b,x,y=1,2,3,4
sub(x,y)
print(a,b,x,y) # 7234