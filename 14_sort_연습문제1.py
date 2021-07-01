# 14_sort_연습문제1.py

scores=[]
stu = 0

man= int(input('학생 수 입력 :'))
for i in range(man):
    num=int(input('학생%d 점수 입력 : '%(i+1)))
    scores.append(num)
    if num >=80:
        stu +=1
tot = sum(scores)
avg = tot/len(scores)
scores.sort(reverse=True)
print('총점 : ',tot)
print('평균 : %.2f'%avg)
print('80점 이상 학생 : %d명'%stu)
print('점수 내림차순 정렬 : ', scores)