#03_function_return.py

# 함수 정의 : 반환값이 있는 함수
# 반환값은 함수 호출 후 함수 내부 문장을 실행하고 실행된 결과를
# 함수를 호출한 지점으로 반환하는 값

# 함수 정의
# 함수 이름 : sum
# 함수 기능 : 사용자로부터 두개의 정수를 입력받아 더한 결과를 반환하는 함수

def sum() :
    num1 = int(input("정수 1 입력 : "))
    num2 = int(input("정수 2 입력 : "))
    return num1+num2

# 함수 호출 했을 대 결과가 반환되는 함수면 결과값이 호출함수 이름 위치로 반환되고
# 반환된 값을 변수에 저장해 볼 것
total=sum()
print('sum()함수를 호출해서 반환받은 값은 %d 입니다.'%total)

print('sum()함수를 호출해서 반환받은 값을 바로 출력합니다. 그 값은 %d 입니다.'%sum())

## 반환값이 없는 경우 변수에 저장하면?
def show():
    print('안녕하세요')

show()

result = show()
print(result)

print(show())