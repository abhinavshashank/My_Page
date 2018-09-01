'''2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?

Value =1366 '''

def digits(n):
    s = 0
    while n > 0:
        s = s + (n % 10)
        n = int(n/ 10)
    return s

print(digits(pow(2,1000)))
