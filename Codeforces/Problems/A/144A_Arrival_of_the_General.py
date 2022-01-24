def lstInp():
    return [int(x) for x in input().split()]
 
n = int(input())
arr = lstInp()
mn,mx = min(arr), max(arr)

#can reverse the arr too here to get the min index
for i in range(n):
    if arr[i] == mn:
        mn_ind = i+1
mx_ind = arr.index(mx)

cnt = n-mn_ind + mx_ind

if mn_ind<=mx_ind:
    cnt-=1

print(cnt)