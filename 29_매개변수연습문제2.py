# 28_매개변수연습문제2.py
from random import randint
def gbb_game():
    you = int(input("You 입력 (1: 가위, 2: 바위, 3: 보) : "))
    com = randint(1,3)
    if you == com :
        print("비겼습니다.")
        print("Com : ", com)
    elif (you== 3 and com == 2) or (you == 2 and com == 1) or (you == 1 and com == 3):
        print("당신이 이겼습니다.")
        print("Com : ", com)
    else :
        print("컴퓨터가 이겼습니다.")
        print("Com : ", com)
gbb_game()