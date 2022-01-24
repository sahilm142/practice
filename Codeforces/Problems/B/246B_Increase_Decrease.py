n = int(input())
arr = list(map(int, input().split()))
sm = sum(arr)
res = n if sm%n==0 else n-1
print(res)