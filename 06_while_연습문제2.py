num = int(input("마지막 숫자를 입력하세요: "))
num1 = num
sumx = 0
while True : # 조건이 무조건 참
    if num1 %2 != 0 :
        sumx = sumx + num1
    num1= num1-1
    if num1 == 0 :
        break
print("1부터 ", num, "까지의 홀수의 합은 ", sumx, "입니다.")
