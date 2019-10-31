# -*- coding: utf-8 -*-

"""
problem statement

https://www.hackerrank.com/challenges/no-idea/problem

"""

n,m = input().split()
arr = [ int(i) for i in input().split()]
A = {int(i) for i in input().split()}
B = {int(i) for i in input().split()}
happiness = 0
for i in arr:
    happiness +=(i in A)-(i in B) 

print(happiness)
    
