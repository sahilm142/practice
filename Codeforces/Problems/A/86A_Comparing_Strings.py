s1=input()
s2=input()
flg=0
res = 0
if len(s1)!=len(s2):
    flg=1
else:
    a,b='',''
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            res+=1
            if res == 1:
                a,b=s1[i],s2[i]
            elif res==2:
                if s1[i]!=b or s2[i]!=a:
                    #print(a,b, s1[i], s2[i])
                    flg=1
            elif res>2:
                flg=1
                break
print('YES' if res == 2 and flg == 0 else 'NO')

'''
rtfabanpc
atfabrnpc

'''