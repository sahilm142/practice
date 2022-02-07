def solve(s,n,k):
	rev = s[::-1]
	if s == rev or k==0:
		return 1
	else:
		return 2
t=int(input())
while t:
	n,k=map(int, input().split())

	#a =list(map(int, input().split()))
	#b =list(map(int, input().split()))
	s = input()
	print(solve(s,n,k))
	t-=1