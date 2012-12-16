from projeuler.math.integer import gen_abundant
import itertools as it

abundants = gen_abundant()

n = 0

"""
Apparently it can be proven that 28123 is the largest
number that cannot be written as the sum of two abundant
numbers.

This is left as an exercise to the reader :)
"""
MAX_NON_SUM_TWO_ABUNDANT = 28123
abundant_set = set()
while n < MAX_NON_SUM_TWO_ABUNDANT:
  n = next(abundants)
  abundant_set.add(n)

abundant_sums_set = set()
for p in it.combinations_with_replacement(abundant_set, 2):
  if sum(p) < MAX_NON_SUM_TWO_ABUNDANT:
    abundant_sums_set.add(sum(p))

non_abudant_sums_set = set(xrange(MAX_NON_SUM_TWO_ABUNDANT+1)) - abundant_sums_set
print repr(sorted(filter(lambda x: x % 2 == 1, abundant_set)))
print repr(sorted(abundant_set))
print repr(sorted(non_abudant_sums_set))
print sum(non_abudant_sums_set)

