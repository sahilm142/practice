n1 = input()
n2 = input()
res = []
for i in range(len(n1)):
    if n1[i]==n2[i]:
        res.append('0')
    else:
        res.append('1')
print(''.join(res))