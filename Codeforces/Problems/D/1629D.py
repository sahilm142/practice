def solve():
    n=int(input())
    s = set()
    s2 = set()
    flg=0
    for i in range(n):
        #print(s)
        x = input()

        if flg==1:
            continue
        n = len(x)
        xr = x[::-1]
        if x==xr or xr in s or n==1:
            flg=1
            #reverse of x with some char appended i.e. x=ab and some str bac already in s
        if n==2:
            if xr in s2:
                flg=1
        if n==3:
            if xr[:2] in s:
                flg=1
            s2.add(x[:2])
        s.add(x)
        
    if flg==0:
        print('NO')
    else:
        print('YES')
 
t=int(input())
 
while t:
    solve()
    t-=1

'''
6
5
zx
ab
cc
zx
ba
2
ab
bad
4
co
def
orc
es
3
a
b
c
3
ab
cd
cba
2
ab
ab

''' 