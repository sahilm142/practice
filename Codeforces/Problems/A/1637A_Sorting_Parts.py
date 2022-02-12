def solve(arr):
    newarr = sorted(arr[1:])

    if newarr == arr[1:] and arr[0]<=newarr[0]:
        print('NO')
    else:
        print('YES')

t = int(input())
while t:
    n = int(input())
    arr = list(map(int, input().split()))
    solve(arr)

    t-=1