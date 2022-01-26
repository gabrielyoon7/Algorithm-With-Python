#최소, 최대
temp=int(input())
numbers=input().split(" ")
max=int(numbers[0])
min=int(numbers[0])
for number in numbers:
    num=int(number)
    if num > max:
        max = num
min=max
for number in numbers:
    num=int(number)
    if num < min:
        min = num
print(min,max)