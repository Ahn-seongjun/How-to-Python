
coin = 10000
sing = 0
while coin > 0 :
    sing += 1
    coin -= 2000
    print("노래를 ", sing, "곡 불렀습니다.")
    if coin > 0 :
        print("현재 ", coin, "원 남았습니다.")
    else :
        print("잔액이 없습니다. 종료합니다.")

# 다른 방법

song = 2000
money = 10000
count = 0

while money != 0 :
    count += 1
    money = money - song
    print("노래를 "+str(count)+"곡 불렀습니다.")

    if money == 0 :
        print("잔액이 없습니다. 종료합니다.")
        break
    else :
        print("현재"+str(money)+"원 남았습니다.")