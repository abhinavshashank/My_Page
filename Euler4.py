'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
Value =906609'''

def palindrome(num):
    if(num==num[::-1]):
        return 1
        
largestpalin=0
    
for i in range(999,99,-1):
    for j in range(999,99,-1):
        x=i*j
        if(palindrome(str(x))==1):
            if(x>largestpalin):
                largestpalin=x
print(largestpalin)
