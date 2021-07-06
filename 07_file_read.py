# 07_file_read.py
# read()함수 : 내용 전체를 읽어서 1개의 문자열로 반환

f= open("test.txt",'r')
data = f.read()
print(data)

print(type(data))
print(len(data))

# 1개 문자씩 출력
for ch in data:
    print(ch)