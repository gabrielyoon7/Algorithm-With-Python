#한수

count=0
n=input()
for i in range(1,int(n)+1):
    numList = list(map(int, str(i)))
    # print(numList)
    if(len(numList)<=2):
        count+=1
    else:
        temp=[]
        # print(numList)
        for j in range(len(numList)-1):
            temp.append(numList[j]-numList[j+1])
        isSame=True
        for j in temp:
            if j != temp[0]:
                isSame=False
                break
        if isSame:
            count+=1

print(count)
