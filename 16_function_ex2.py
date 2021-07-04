# 16_function_ex2.py

def get_area():
    A = int(input('가로길이 입력 : '))
    B = int(input('세로길이 입력 : '))
    return A*B
tot = get_area()
print('사각형의 면적 : %d'%tot)