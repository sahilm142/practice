n = int(input())
num = list(input())
num1,num2=[],[]
for i in range(n):
    num1.append(int(num[i]))
    num2.append(int(num[n+i]))

flg=True
num1.sort()
num2.sort()
#print(num1,num2)
for i in range(n):
    if num1[i]<=num2[i]:
        flg = False
if flg:
    print('YES')
else:
    flg = True
    for i in range(n):
        if num1[i]>=num2[i]:
            flg=False
    if flg:
        print('YES')
    else:
        print('NO')
