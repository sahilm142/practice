def listInp():
    return [int(x) for x in input().split()]
n=3
arr = [[0]*n for _ in range(n)]

dx = [ 0, -1, 0,  1]
dy = [ -1, 0, 1, 0]

res = [[0]*n for _ in range(n)]
for i in range(n):
    arr[i] = listInp()
print(arr)

for i in range(n):
    for j in range(n):
        res[i][j]
        for x in dx:
            for y in dy:
                if (i+x<n and i+x>=0) and (j+y>=0 and j+y<n):
                    res[i][j] += arr[i+x][j+y]
for i in range(n):
    for j in range(n):
        print(res[i][j]%2, end ='')
    print()
