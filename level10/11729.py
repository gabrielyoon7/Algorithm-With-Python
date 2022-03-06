#하노이 탑 이동 순서
route=[]
def hanoi(num, first, second, third):
    if num==0:
        return
    hanoi(num-1, first, third, second)
    route.append(str(first)+" "+str(third))
    hanoi(num-1, second, first, third)

N=int(input())
hanoi(N,1,2,3)
print(len(route))
for i in route:
    print(i)