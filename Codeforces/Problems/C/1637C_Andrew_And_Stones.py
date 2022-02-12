def solve(arr,n):
    cntone,res = 0,0
    if n==3:
        return -1 if arr[1]%2==1 else arr[1]//2
    for i in range(1,n-1):
        if arr[i]==1:
            cntone+=1
        res += (arr[i]+1)//2
    if cntone == n-2:
        return -1

    return res

t = int(input())
while t:
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr,n))
    t-=1