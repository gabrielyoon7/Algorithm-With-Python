#팩토리얼
def factorial(n):
    if n!=0:
        tmp=n*factorial(n-1)
        return tmp
    return 1

print(factorial(int(input())))
