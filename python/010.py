from projeuler.math.integer import gen_primes

primes = gen_primes()
p = next(primes)
s = 0
while p < 2000000:
  s += p
  p = next(primes)

print s
