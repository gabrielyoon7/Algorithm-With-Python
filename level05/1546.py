#평균
temp = int(input())
scores=input().split(" ")
max=int(scores[0])
for i in scores:
    if max < int(i):
        max=int(i)
print(max)