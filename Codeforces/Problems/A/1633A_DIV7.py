def solve(n):
	x = n%7
	y = n//10
	if x==0:
		return n
	res = n+(7-x)
	if res//10 != y:
		res = n-x
	return res

t=int(input())
while t:
	n=int(input())
	#a =list(map(int, input().split()))
	#b =list(map(int, input().split()))
	
	print(solve(n))
	t-=1