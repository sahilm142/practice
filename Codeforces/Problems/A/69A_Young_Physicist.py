def lstInp():
    return [int(x) for x in input().split()]
 
n = int(input())
x,y,z=0,0,0
 
for i in range(n):
    vec = lstInp()
    x+=vec[0]
    y+=vec[1]
    z+=vec[2]
    
if x==0 and y==0 and z==0:
    print("YES")
else:
    print("NO")