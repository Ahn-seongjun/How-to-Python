# 10_append_연습문제2.py

scores=[]
for i in range(5):
    num=int(input('학생%d 점수 입력 : '%(i+1)))
    scores.append(num)
tot = sum(scores)
avg = tot/len(scores)
print('총점 : ',tot)
print('평균 : %.2f'%avg)


