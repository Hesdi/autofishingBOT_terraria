import collections

c = collections.Counter('abcdaab')

for letter in 'abcde':
    print('%s : %s' %(letter, c[letter]))