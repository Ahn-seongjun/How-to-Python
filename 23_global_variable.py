# 23_global_variable.py

# 전역변수를 함수 내부에서 변경하려면 global 키워드 사용

a = 1 # 함수 밖에서 정의된 전역변수 a

def add():
    global a # a 변수는 전역변수고 함수 내에서 수정할수도 있다라는 키워드
    a=a+1
    c=a+b
    print(a)
    print(b)
    print(c)

b=3 # 함수 밖에서 정의된 전역변수 b - 함수 정의 후 생성되어도 함수 내에서 사용가능

add()
add()
print(a)