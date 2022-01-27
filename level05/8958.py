#	OX퀴즈

num = int(input())
for i in range(num):
    result=input()
    score=0
    stack=1
    for j in result:
        if j =='O':
            score+=stack
            stack+=1
        else:
            stack=1
    print(score)

