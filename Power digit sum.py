""" Problem Statement
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""
num= 2**1000
sum=0
temp = num
for n in range(0,len(str(num))):
    value = divmod(temp,10)
    temp = value[0]
    sum +=value[1]
print sum
