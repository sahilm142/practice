def solve(l,r,a):
    x = 0
    #answer will be either r, l or x-1 where x is (r//a)*a  
    mult = (r//a)*a
    if l<=mult-1:
        x = (mult-1)//a + (mult-1)%a 
    return max(r//a+r%a, l//a+l%a,x)


t=int(input())
while t:
    l,r,a = list(map(int, input().split()))
    print(solve(l,r,a))
    t-=1
