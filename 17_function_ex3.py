# 17_function_ex3.py

def order():
    price = int(input('상품가격 입력 : '))
    EA = int(input('주문수량 입력 : '))
    cost = price * EA
    return price,EA,cost


price,EA,cost = order()
print('---------------')
print('상품가격 : %d원'%price)
print('주문수량 : %d개'%EA)
print('주문액 : %d원' %cost)
