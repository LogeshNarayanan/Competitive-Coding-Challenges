"""
Alice wrote a sequence of words in CamelCase as a string of letters, , having the following properties:

It is a concatenation of one or more words consisting of English letters.
All letters in the first word are lowercase.
For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
Given , print the number of words in  on a new line.
"""

string = raw_input().strip()
word = 1
for i in range (0,len(string)):
  if(ord(string[i]) < 97):
    word+=1
print word
