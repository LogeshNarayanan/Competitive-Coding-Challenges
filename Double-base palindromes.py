""" ----- Problem Statement -----
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def palindrome(num):
  pal = 0
  while(num):
    temp = num % 10
    num /=10
    pal = (pal*10) + temp
  return pal
sum =0
for i in range(1,1000000):
  decimalPal = palindrome(i)
  if(i == decimalPal):
    binval = int(bin(i)[2:])
    binpal = palindrome(binval)
    if(binval == binpal):
      sum +=i
print sum 
    
