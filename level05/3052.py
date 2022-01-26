#나머지
left=[]
for i in range(0,10):
    temp=int(input())%42
    if temp in left:
        continue
    else:
        left.append(temp)
print(len(left))