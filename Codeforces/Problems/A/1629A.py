def findInd(a,x):
    for i in range(len(a)):
        if a[i]<=x and a[i]!=1001:
            a[i] = 1001
            return i
    return -1

def solve(a,b,k,n):
    x=k
    for i in range(n):
        ind = findInd(a,x)
        if ind == -1:
            return x
        x+=b[ind]
    return x


t=int(input())

while t:
    n,k = map(int, input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    print(solve(a,b,k,n))
    t-=1