# Problem link --> https://www.hackerrank.com/contests/projecteuler/challenges/euler020

from __builtin__ import raw_input
a = int(raw_input())
series = {0:1,1:1}
for i in range(a):
    num = int(raw_input())
    if (series.has_key(num) == False):
        size = series.__len__()
        for j in range(size,num+1):
            series[j]= j * series[j-1]
    value = series[num]
    sum = 0
    while(value>0):
        temp = value%10;
        sum+=temp;
        value /=10; 
    print sum
