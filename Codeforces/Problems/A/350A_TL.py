n,m = map(int, input().split())
r = list(map(int, input().split()))
w = list(map(int, input().split()))
tl = max(r)
v = min(r)
mn = min(w)
flg=0
if max(2*v, tl)<mn:
    print(max(2*v,tl))
else:
    print(-1)

'''
2 5
45 99
49 41 77 83 45

'''