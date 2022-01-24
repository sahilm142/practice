
#from math import sqrt

#def checkPrime(x):
 #   isPrime = True
  #  for i in range(2, int(sqrt(x)) + 1 ):
   #     if x%i==0:
    #        isPrime = False
     #       break
    #return isPrime
n=int(input())
#print n prime numbers
#find some seq that satisfies here 2*n to 2*n+(n-1), smallest being 2*n it can't divide any number from 2*n to 2*n+n-1
#MX = 10**7
cnt=0
for i in range(n):
    print(2*n+i, end=' ')