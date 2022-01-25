#더하기 사이클
num=int(input())
num_copy=num
count=0
while True:
    a=num_copy//10
    b=num_copy%10
    temp= a + b
    # print(a,"+",b,"=",result)
    num_copy=(b)*10+(temp % 10)
    # print(num_copy)
    count+=1
    if num==num_copy:
        break
print(count)