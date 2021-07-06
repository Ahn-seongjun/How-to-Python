# 01_file_create.py

# 파일 생성 : 파일명만 적으면 현재 디렉터리에 생성
# 파일객체변수명 = open(파일명, 모드"w")
# 위 코드 실행 후 파일 핸들링 위해서는 파일 객체변수명을 사용함
# 파일 생성
# 파일을 쓰기 모드(w)로 연다
# 해당 파일이 존재하지 않으면 새로 생성하고
# 존재하면 덮어 씀 (기존 내용 없어짐)

# f= open('file1.txt','w') # file1.txt 파일이 현재 폴더에 없으면 새 파일 생성, 있으면 해당파일의 내용을 지우고 열어준다
# f.close()

# 현재폴더와 다른 폴더에 저장하고 싶으면 전체경로를 적으면 됨
# f= open('../file2.txt','w')
# f.close()

# f=open('c:/file1.txt','w') # 절대경로 : 최상위 디렉토리부터 모든 경로 표시
# f.close()

# f=open('../../file_test.txt','w') # 상대경로 - 현재 위치 기준
# f.close()

# 경로에 표시된 디렉터리명이 실제 없으면 : 에러
# f = open("../abc/test.txt",'w') # 상대경로 현재 폴더의 상위폴더에서 abc폴더를 찾고 그안에 test.txt 생성
# f.close()