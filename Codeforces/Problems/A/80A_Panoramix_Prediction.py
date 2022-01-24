def listInput():
    return [int(x) for x in input().split()]

def isPrime(n):
    is_prime = True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            is_prime = False
    return is_prime

n,m = listInput()
flg = False
for i in range(n+1, m+1):
    check = isPrime(i)
    if check and i == m:
        flg = True
        break
    elif check and i!=m:
        break
print('YES' if flg else 'NO')

#primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
#if m in primes and primes.index(n)+1 == primes.index(m):
 #   print('YES')
#else:
 #   print('NO')