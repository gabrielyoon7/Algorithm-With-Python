#최댓값
current_index=0
max=0
numbers=[]
index=0
for i in range(0,9):
    temp=int(input())
    numbers.append(temp)
    if max<temp:
        max=temp
        index=i+1

print(max)
print(index)