# 25_지역변수전역변수.py

def var_test(a):
    print(a,"메모리 주소 : ",id(a))
    b=10 # 지역변수
    print(b,'메모리 주소 :',id(b))

# 함수 외부
a = 10
b = 'abc'
var_test(a)
print('전역변수 a', a, '메모리 주소 :',id(a))
print('전역변수 b', b, '메모리 주소 :',id(b))

# 매개변수의 이름을 전역변수의 이름과 같이 사용하지 않는다.