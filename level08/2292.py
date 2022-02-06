#벌집
N=int(input())
if N==1:
    print(N)
else:
    index=1
    n=1
    while index<N:
        index+=6*(n-1)
        n+=1
    print(n-1)
