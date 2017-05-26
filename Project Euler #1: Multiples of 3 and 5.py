def multiple(n): 
    return n*(n+1)/2
def sum(n): 
    return multiple(n/3)*3 + multiple(n/5)*5 - multiple(n/15)*15
for i in xrange(int(raw_input())):
    n = int(raw_input()) - 1
    print sum(n)
