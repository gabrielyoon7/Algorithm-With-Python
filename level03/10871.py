#X보다 작은 수
n,x=map(int,input().split(" "))
numbers=input().split(" ")
for i in numbers:
    if int(i)<x:
        print(str(i), end=" ")