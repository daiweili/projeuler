from projeuler.math.integer import gen_primes

primes = gen_primes()

for i in xrange(10001):
  p = next(primes)

print p
