from projeuler.math.integer import factorize
from operator import mul

factors = {}

"""
Get the highest multiplicity of each prime factor
and multiply them together
"""
for i in xrange(1, 21):
  f = factorize(i)
  for k,v in f.iteritems():
    if k not in factors or factors[k] < v:
      factors[k] = v

print reduce(mul,[k**v for k,v in factors.iteritems()])
