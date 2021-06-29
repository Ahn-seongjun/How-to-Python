sent = input('문장을 입력하세요 : ')
alp = 0
num = 0
spa = 0
oth = 0
for i in sent:
    if i.isalpha() :
        alp +=1
    elif i.isdigit():
        num +=1
    elif i.isspace():
        spa +=1
    else :
        oth +=1
print('알파벳 : %d개\n숫자 : %d개\n스페이스 : %d개\n기타 : %d개'%(alp,num,spa,oth))