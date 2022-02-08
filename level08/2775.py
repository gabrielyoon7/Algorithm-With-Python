#부녀회장이 될테야
T=int(input())
for i in range(T):
    K=int(input())
    N=int(input())
    temp=[]
    for j in range(1,N+1):
        temp.append(j)
    # print(temp)
    for j in range(K):
        floor=[]
        for k in range(1,N+1):
            tmp=0
            for l in range(k):
                tmp+=temp[l]
            floor.append(tmp)
        # print(floor)
        temp=list(floor)
    print(floor[-1])

    
