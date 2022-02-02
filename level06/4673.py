# #셀프 넘버
def d(n):
    numList =list(map(int, str(n)))
    num=n
    for i in numList:
        num+=i
    if num > 10000 or arr[num]==True:
        return
    arr[num]=True
    return d(num)


arr=[False]*10001
for i in range(1,10001):
    d(i)

for i in range(1,len(arr)):
    if arr[i]==False:
        print(i)
