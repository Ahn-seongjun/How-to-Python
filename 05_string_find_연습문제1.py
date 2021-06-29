email = input("이메일 입력 : ")

if email.find("@") == -1:
    print("이메일 형식이 아닙니다.")
elif email.find(".") == -1:
    print("이메일 형식이 아닙니다.")
elif email.find("@") > email.find("."):
    print("이메일 형식이 아닙니다.")
elif email.find("@")+1 == email.find("."):
    print("이메일 형식이 아닙니다.")
elif email.find("@") == 0 :
    print("이메일 형식이 아닙니다.")
elif email.find(".") == len(email)-1 :
    print("이메일 형식이 아닙니다.")
elif email.count("@")>=2 :
    print("이메일 형식이 아닙니다.")
elif email.count(".")>=2 :
    print("이메일 형식이 아닙니다.")
print("입력한 이메일 : %s" %email)