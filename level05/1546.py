#평균
temp = int(input())
scores=input().split(" ")
max=int(scores[0])

for i in scores:
    if max < int(i):
        max=int(i)
# print(max)
sum=0
for i in range(len(scores)):
    scores[i]=(int(scores[i])/max)*100
    sum+=scores[i]
# print(scores)
print(sum/len(scores))
