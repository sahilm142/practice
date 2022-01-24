s = input()
cnt = 0
for c in s:
    if c.isupper():
        cnt+=1
    else:
        cnt-=1
if cnt>0:
    print(s.upper())
else:
    print(s.lower())