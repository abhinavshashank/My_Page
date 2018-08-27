'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
Value= 232792560'''

def gcd(m,n):
    return n and gcd(n, m%n) or m
def lcm(x,y):
    return (x*y)/gcd(x,y)

num=1
for i in range(2,21):
    num=lcm(num,i)
    
print(int(num))
