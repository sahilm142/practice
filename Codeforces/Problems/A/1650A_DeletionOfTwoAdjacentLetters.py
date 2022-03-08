def solve(s,c):
    n=len(s)
    flg = 0
    if n==1 and c==s:
        flg=1

    for i in range(n):
        if s[i]==c:
            if (i)%2==0:
                flg=1
                break
    return 'YES' if flg else 'NO'

t=int(input())
while t:
    s=input()
    c=input()
    print(solve(s,c))
    t-=1