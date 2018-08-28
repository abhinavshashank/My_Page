'''The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
Value=6857 '''

numm = 600851475143;
newnumm = numm;
largestFact = 0;
 
counter = 2
while (counter * counter <= newnumm):
    if (newnumm % counter == 0):
        newnumm = newnumm / counter
        largestFact = counter
    else:
        counter+=1

if (newnumm > largestFact): # the remainder is a prime number
    largestFact = newnumm

print(int(largestFact)
