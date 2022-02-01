#정수 N개의 합
def solve(a: list) -> int:
    total=0
    for i in a:
        total+=i
    return total

if __name__ == '__main__':
    print(solve([1,2,3]))