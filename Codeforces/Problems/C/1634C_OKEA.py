
def solve(n,k):
	flg=0
	if k==1:
		print('YES')
		for i in range(n):
			print(i+1)
		return
	
	if n%2==1:
		print('NO')
		return
	print('YES')
	odd,even=1,2
	for i in range(1, n+1):
		for j in range(1, k+1):
			if i%2==1:
				print(odd, end=' ')
				odd+=2
			else:
				print(even, end = ' ')
				even+=2
		print()

t=int(input())
while t:
	#n=int(input())
	n,k = map(int, input().split())
	solve(n,k)
	t-=1

