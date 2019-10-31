"""
Problem Statement

https://www.hackerrank.com/challenges/merge-the-tools/problem

"""
def merge_the_tools(string, k):
    l = int(len(string)/k)
    for i in range(l):
        v = ''
        for char in string[i*k:i*k+k]:
            if char not in v: v +=char
        print(v)
        
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)