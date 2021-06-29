# 중첩 for 구구단

#구구단 출력 2단부터 9단까지

# for dan in range(2, 10) :
#     for n in range(1,10) :
#         print('%d * %d = %d'%(dan,n,dan*n))
#
#     print()

for n in range(1, 10) :
    for dan in range(2,10) :
        print('%d * %d = %d'%(dan,n,dan*n), end="\t")

    print()