n = int(input())
ld,rd = 0,0
m = n
while m:
    l,r = map(int, input().split())
    ld+=l
    rd+=r
    m-=1
t = min(ld,abs(n-ld))+min(rd, abs(n-rd))
print(t)