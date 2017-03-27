""" ------ Problem Statement ------
n! means n × (n - 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
def fact(num):
  val = 1
  while(num>1):
    temp = num - 1
    val *=num
    num = temp
  return val
value = fact(100)
sum =0
value_string = str(value)
for i in range(0,len(value_string)):
  sum += int(value_string[i])
print sum