#피보나치 수 5
def f(n):
    if n == 0 or n == 1:
        return n
    return f(n-1)+f(n-2)

print(f(int(input())))