def solve(x):
	x = list(x)
	i = len(x)-1
	flg=0
	while i>1:
		num = int(x[i])+int(x[i-1])
		if num >= 10:
			x[i-1] = str(num)
			print(''.join(x[:i]) + ''.join(x[i+1:]))
			flg=1
			break

		i-=1
	if flg == 0:
		num = int(x[0])+int(x[1])
		print(str(num)+''.join(x[2:]))

n=int(input())
while n:
	x=input()
	solve(x)
	n-=1