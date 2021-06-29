inf = input("생일 입력 (연/월/일) : ")
inf_split = inf.split('/')
print('당신은 %s년에 태어났고\n생일은 %s월 %s일 이군요'%(inf_split[0],inf_split[1],inf_split[2]))
