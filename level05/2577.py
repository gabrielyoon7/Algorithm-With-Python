#숫자의 개수
a=int(input())
b=int(input())
c=int(input())
number=str(a*b*c)
count=[0,]*10
for num in number:
    count[int(num)]+=1
for cnt in count:
    print(cnt)