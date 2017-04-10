"""
We consider a word, to be beautiful if the following two conditions are satisfied:

No two consecutive characters are the same.
No two consecutive characters are in the following vowel set: a, e, i, o, u, y. Note that we consider y to be a vowel in this challenge.
"""

w = raw_input().strip()
check = True
for i in range(len(w)-1):
  if(w[i] == w[i+1]):
    print i
    check = False
    break
  if (w[i] == 'a' or w[i] == 'e' or w[i] == 'i' or w[i] == 'o' or w[i] == 'u' or w[i] == 'y'):
    if (w[i+1] == 'a' or w[i+1] == 'e' or w[i+1] == 'i' or w[i+1] == 'o' or w[i+1] == 'u' or w[i+1] == 'y'):
      check = False
      break
if(check):
  print "Yes"
else:
  print "No"
