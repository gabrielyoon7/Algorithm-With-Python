#분해합 
N = int(input())
answer=0
for i in range(1,N+1):
    tmp=i
    tmp2=0
    for j in str(i):
        tmp2+=int(j)
    if tmp+tmp2 == N : 
        answer=tmp
        break
    answer=0
print(answer)