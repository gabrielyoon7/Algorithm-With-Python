N,M=map(int,input().split())
cards=list(map(int,input().split()))
max=0
tmp_i=0
tmp_j=0
tmp_k=0
# print(cards)
for i in range(N):
    for j in range(N):
        for k in range(N):
            tmp = cards[i]+cards[j]+cards[k]
            if i!=j and i!= k and j!=k and tmp <= M and tmp>max:
                    max=tmp             
print(max)