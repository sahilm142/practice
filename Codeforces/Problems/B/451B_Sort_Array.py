n=int(input())
arr = list(map(int, input().split()))
flg=0
L=0
while L<n-1 and arr[L]<=arr[L+1]:
	L+=1
R = L
while R<n-1 and arr[R]>arr[R+1]:
	R+=1
#arr[L:R+1].reverse()
arr[L:R+1] = arr[L:R+1][::-1]
print(arr)

for i in range(n-1):
	if arr[i]>arr[i+1]:
		flg=1
		break

if flg==1:
	print('no')
else:
	print('yes')
	print(L+1,R+1)
