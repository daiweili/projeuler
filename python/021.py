from projeuler.math.integer import get_factors

amicable = set()
for i in xrange(10000):
  s = sum(get_factors(i)) - i
  s2 = sum(get_factors(s)) - s
  if s2 == i and s != i:
    amicable.add(i)
    amicable.add(s)

print amicable
print sum(amicable)
