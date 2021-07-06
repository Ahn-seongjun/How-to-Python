# 05_file_readline.py

# 파일 읽기 방법
# readline()
# 1개 행씩 읽어 오기
# 1행 끝에 ‘\n’ 포함
# readlines() :
# 모든 행을 읽어 라인 별로 잘라서 리스트 생성
# 1개 행이 1개 요소
# [‘..’, ‘…’, ‘…’, …, ‘…’]
# read()
# 내용 전체를 읽어서 문자열로 반환

# readline() 함수를 이용해서 1개 라인 읽어오기
print("---첫 번째 행 읽기 ---")

f1 = open("test.txt","r")
line = f1.readline() # 첫번째 라인 1개 읽어오기
print(line)
f1.close()

# readline() 함수를 이용해서 전체라인 읽어오기
# 1행씩 읽고 출력을 반복 - 더 이상 파일의 내용이 없을 때까지

# print("---파일 전체 읽기---")
# f2 = open("test.txt",'r')

# while True: # 무한반복 (몇행인지 알수없음)
#     line =f2.readline()
#     if not line :
#         break
#     print(line,end ='')
# f2.close()

# 파일 전체 라인을 읽어와서 다른 파일에 쓰는 코드
# 2개 파일 필요
f2 = open("test.txt",'r') # 원본
f3 = open('test_write.txt','a',encoding='utf-8')

while True: # 무한반복 (몇행인지 알수없음)
    line =f2.readline()
    if not line :
        break
    f3.write(line)
    print(line,end ='')
f2.close()