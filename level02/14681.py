#	사분면 고르기
x,y = map(int, input().split())

if x>0:
    if y>0:
        print("1")
    else:
        print("4")
else:
    if y>0:
        print("2")
    else:
        print("3")