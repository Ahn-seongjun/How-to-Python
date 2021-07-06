# 02_exception1.py
# 예외처리 예제

# 에러 종류와 상관없이 모든 에러처리
# try-except 구문

try:
    # print(10/0) # 에러가 발생하면 무조건
    print("나이:"+23+"살")
except: #본 구문으로 포거스가 넘어옴
    print("오류 발생")

print("=======Exception 클래스 사용========")

try:
    # print(10/0) # 에러가 발생하면 무조건
    print("나이:"+23+"살")
except Exception: #본 구문으로 포거스가 넘어옴
    print("오류 발생")

# 에러 종류 명시

try:
    print(10/0) # 에러가 발생하면 무조건
    print("나이:"+23+"살")
except ZeroDivisionError: #본 구문으로 포거스가 넘어옴
    print("오류 발생")

# 숫자를 입력하지 않은 경우
try:
    num = int(input("숫자를 입력하세요: "))
except ValueError as e:
    print("숫자가 아닙니다",e) # 오류가 난 부분 붙이기

# 여러개의 except 구문을 생성 : 첫번째 에러만 처리됨
a=[1,2,3]

try:
    print(a[4])
    print(10 / 0)
except ZeroDivisionError as e:
    print('0으로 나눌 수 없습니다.')
except IndexError as e:
    print(e)