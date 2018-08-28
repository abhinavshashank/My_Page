'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
Value=104743'''

def isprime(num):
    for i in range(2, int(num/2)+1):
        if(num%i==0):
            return 1
    return 0

def nthprimenumber(n):
    if n==1:
        return 2
    count = 1
    num = 3
    while(count <= n):
        if isprime(num==0):
            count +=1
            if count == n:
                return num
        num +=2
print(nthprimenumber(10001))
