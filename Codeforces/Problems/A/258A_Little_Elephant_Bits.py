s=list(input())
if '0' in s:
    ind = s.index('0')
    print(''.join(s[:ind])+''.join(s[ind+1:]))
else:
    print(''.join(s[:-1]))

