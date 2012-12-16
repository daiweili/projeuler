from projeuler.string import int_to_eng

def remove_whitespace(s):
  return s.replace(' ', '')

letters = 0
for i in xrange(1, 1001):
  letters += len(remove_whitespace(int_to_eng(i)))
print letters
