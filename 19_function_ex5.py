# 19_function_ex5.py


def get_inerest(deposit, int_rate):
    interest = deposit * int_rate / 100
    return int(interest)

dps = int(input("예금액 입력 : "))
rate = float(input("이자율 입력(%) : "))

tot = format(get_inerest(dps,rate),",")

print("이자액 : %s원"%tot)

