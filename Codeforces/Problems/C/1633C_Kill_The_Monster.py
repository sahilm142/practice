import math
def checkWinner(hc,dc,hm,dm):
	turn_hero = math.ceil(hm/dc)
	turn_monester = math.ceil(hc/dm)
	return turn_hero<=turn_mon

def solve(hc,dc,hm,dm,k,w,a):
	flg = 0
	for i in range(k+1):
		h = hc + i*a
		d = dc + (k-i)*w
		if checkWinner(h,d,hm,dm):
			flg=1
			break

	print('YES' if flg else 'NO')

t=int(input())
while t:
	#n=int(input())
	hc,dc = map(int, input().split())
	hm,dm = map(int, input().split())
	k,w,a = map(int, input().split())
	solve(hc,dc,hm,dm,k,w,a)
	t-=1

'''
1
25 4
12 20
1 1 10
'''