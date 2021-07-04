# 28_매개변수연습문제1.py

def order():
    pri = int(input("상품 가격 입력 : "))
    qty = int(input("주문 수량 입력 : "))
    amo = pri*qty
    if amo >= 100000 :
        dis = amo * 0.1
    elif 50000<=amo< 100000:
        dis = amo * 0.05
    else :
        dis = amo * 0
    tot = amo - dis
    return pri,qty,amo,dis, tot

price,qty,amount,discount,total = order()
print('---------------')
print('주문액 : %d원'%amount)
print('할인액 : %d개'%discount)
print('지불액 : %d원' %total)


