# 06_file_readlines.py

# readlines() 함수를 이용해서 전체 라인 읽어오기

print("------전체라인 읽고 출력----------")
f1 = open("test.txt",'r')
lines = f1.readlines()
print(lines)
f1.close()

print("------전체라인 읽어서 1행씩 출력---------")
f2 = open("test.txt",'r')
lines = f2.readlines()

for line in lines:
    print(line,end="")

f2.close()

print("\n------파일객체의 특징 : 반복문에서 반복요소로 사용가능---------")

f3 = open("test.txt",'r')

for line in f3:
    print(line, end='')