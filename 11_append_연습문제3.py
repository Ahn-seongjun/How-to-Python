# 11_append_연습문제3.py

scores=[]
stu = 0
for i in range(5):
    num=int(input('학생%d 점수 입력 : '%(i+1)))
    scores.append(num)
    if num >=80:
        stu +=1
tot = sum(scores)
avg = tot/5

print('총점 : ',tot)
print('평균 : ',avg)
print('80점 이상 학생 : %d명'%stu)