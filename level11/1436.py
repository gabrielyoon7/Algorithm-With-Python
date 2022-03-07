#영화감독 숌

N = int(input())
answer=0
count=0
while count < N:
    answer+=1
    if str(answer).find('666')!=-1:
        count+=1
print(answer)