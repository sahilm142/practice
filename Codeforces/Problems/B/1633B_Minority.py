def solve(s):
	n = len(s)
	z,o,ans = 0,0,0
	for i in range(n):
		if s[i] == '1':
			o+=1
		else:
			z+=1
	if o!=z:
		ans = min(o,z)
	if o==z and o>=1:
		ans=o-1
	return ans


t=int(input())
while t:
	s = input()
	print(solve(s))
	t-=1