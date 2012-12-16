import itertools as it

p = it.permutations([0,1,2,3,4,5,6,7,8,9])
for i in xrange(1000000):
  x = next(p)
print ''.join(map(str,x))
