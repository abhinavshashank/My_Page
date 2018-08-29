'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Value=142913828922'''

def isprime(num):
    for i in range(2, int(num/2)+1):
        if(num%i==0):
            return 1
    return 0
n=2000000
sum=0
for i in range (2,n):
    if(isprime(i)==0):
        um+=i
print(sum)
