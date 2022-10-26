import collections

c = collections.Counter()
with open("poem.txt") as f:
    for line in f:
        c.update(line.rstrip().lower())

print('Most common letters in poem.txt:')
for letter, count in c.most_common(3):
    print('{}: {:>7}'.format(letter, count))