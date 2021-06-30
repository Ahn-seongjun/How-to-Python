# 13_append_연습문제5.py

item=[]
while True:
    product = input('상품 등록 (엔터키 누르면 종료) :')
    item.append(product)
    if product == "" :
        break

print('등록된 상품 : ',item)