#수 정렬하기
N=int(input())
num=[]
for i in range(N):
    num.append(int(input()))
for i in range(N):
    min_index=i
    for j in range(i+1, N):
        if num[min_index]>num[j]:
            min_index=j
    num[i], num[min_index] = num[min_index], num[i]
for i in num:
    print(i)