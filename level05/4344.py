#평균은 넘겠지
C=int(input())
for c in range(C):
    students = input().split(" ")
    sum_score=0
    for i in range(1,int(students[0])+1):
        sum_score += int(students[i])
    average=sum_score/int(students[0])
    count=0
    for i in range(1,int(students[0])+1):
        if average < int(students[i]):
            count+=1
    percentage = round(count/int(students[0])*100, 3)
    print(format(percentage, '.3f')+"%")
