from collections import Counter

def solve(s):
	m = Counter(s)
	m = sorted(m.items(), key=lambda i: i[1], reverse=True)
	for (a,b) in m:
		if b==2:
			print(a,end='')
	for (a,b) in m:
		print(a,end='')

n=int(input())
while n:
	s=input()
	solve(s)
	print()
	n-=1