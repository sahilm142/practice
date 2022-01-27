y,k,n=map(int, input().split())
flg=0
for i in range(k,n+1,k):
	if i>y:
		print(i-y, end=' ')
		flg=1
if flg==0:
	print(-1)