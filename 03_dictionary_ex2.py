# 03_dictionary_ex2.py

word = {}

while True :
    eng = input("\n영어 단어 등록 (종료는 quit) : ")
    if eng == 'quit' :
        break # 종료
    elif eng not in word :
        kor = input('%s의 뜻 입력 : '%eng)
        word[eng]=kor
    else :
        print('%s는 이미 등록된 단어 입니다.'%eng)
print()

print("사전에서 단어를 검색하세요.")
while True:
    eng = input("검색할 단어 입력(종료는 quit) : ")
    if eng == "quit":
        break
    elif eng in word :
        print("%s의 뜻은 %s 입니다."%(eng, word[eng]))
    else :
        print("%s 는 사전에 없는 단어 입니다."%eng)
print("\n종료합니다")