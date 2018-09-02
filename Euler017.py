'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

Value= 21224'''

number = {
    1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',
    8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',
    14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',
    18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',
    50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',
    100:'hundred',1000:'thousand'}

tally = 0
for n in range(1,1001):
    x = str(n)    
    if len(str(n)) == 1:
        k = len(number[n])
        
        
    elif len(str(n)) == 2:
        x1 = x[0:1]
        x2 = x[1:2]
        if n < 20:
            k = len(number[n])
            
        else:
            if x2 == '0':
                k = len(number[n])
                
            else:
                x1a = str(x1 + '0')
                k = len(number[int(x1a)]) + len(number[int(x2)])
                
                
                
    elif len(str(n)) == 3:
        x1 = x[0:1]
        x2 = x[1:2]
        x3 = x[2:3]
        x1a = str(x2 + '0')
        x1aa = str(x2 + x3)
        if x1 == '1' and x2 == '0' and x3 == '0':
                k = len(number[1]) + len(number[100])
        elif x2 == '0' and x3 == '0':
                k = len(number[int(x1)]) + len(number[100])
        elif x2 == '0' and x3 != '0':
                k = 3 + len(number[int(x1)]) + len(number[100]) + len(number[int(x3)])
        elif x2 != '0' and x3 == '0':
                k = 3 + len(number[int(x1)]) + len(number[100]) + len(number[int(x1a)])
        elif x2 == '1' and x3 != '0':
            k = 3 + len(number[int(x1)]) + len(number[100]) + len(number[int(x1aa)])
        else:
            k = 3 + len(number[int(x1)]) + len(number[100]) + len(number[int(x1a)]) + len(number[int(x3)])
    else:
        k = len(number[1]) + len(number[1000])
        

    tally= tally + k
print (tally)
