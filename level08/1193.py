#분수찾기
import sys
input = sys.stdin.readline
X = int(input())
index=0
deep=0
isEnd=False
while True:
    deep+=1
    # print('deep : %d' %deep)
    if deep%2==1:
        x=deep-1
        y=0
    else:
        x=0
        y=deep-1
    # print('x is %d, y is %d' %(x,y))
    for i in range(deep):
        index+=1
        # print(index)
        if X==index:
            isEnd=True
            break
        if deep%2==1:
            x-=1
            y+=1
        else:
            x+=1
            y-=1
    if isEnd:
        break
print('%d/%d' %(x+1, y+1))