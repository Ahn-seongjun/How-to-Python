# 03_while_7을 입력하면 종료.py

# 사용자로부터 숫자를 입력받아 입력된 숫자가 7이면 종료문자를 내보내고 프로그램을 종료
# 7이 아니면 다시 입력을 받는다(while문을 이용해서 작성)

# 입력양식
# 처음 입력 시
# 숫자 입력 : 5

# 다시 입력 시
# 다시 입력 : 7

# 출력양식
# 7 입력! 종료

# 입력 코드

num = int(input('숫자 입력(점수): '))

# 입력숫자가 7인지 확인

# 다시 입력 반복

while num != 7 :
    num = int(input("다시 입력 : "))

print(num,'입력!종료')