def countOdd(l,r):
    if l%2==1 or r%2==1:
        return (r-l)//2+1
    else:
        return (r-l)//2

def solve(l,r,k):
    co = countOdd(l,r)
    if r-l == 0 and r!=1:
        return 'YES'
    if co>k:
        return 'NO'
    else:
        return 'YES'

t=int(input())

while t:
    l,r,k = map(int, input().split())
    print(solve(l,r,k))
    t-=1