n,k = map(int, input().split())
arr = list(map(int,input().split()))
#Min sum subarray of size k
start_ind, end_ind = 0,k-1
minSum = float('inf')
res = 0
sm = sum(arr[start_ind:end_ind])
while end_ind<n:
    sm+=arr[end_ind]
    if minSum > sm:
        minSum = sm
        res = start_ind
    sm -= arr[start_ind]
    start_ind+=1
    end_ind+=1
print(res+1)

'''
7 3
1 2 6 1 1 7 1
3

1 1
100

'''