#ACM 호텔
T = int(input())
for i in range(T):
    H, W, N = map(int,input().split())
    if N%H==0:
        h=(N//H)
        w=H
    else:
        h=(N//H)+1
        w=N%H

    if h<10:
        print(str(w)+'0'+str(h))
    else:
        print(str(w)+str(h))