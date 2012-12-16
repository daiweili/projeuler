from math import sqrt, floor
from collections import defaultdict

def gen_primes():
  yield 2
  primes = [2,3]
  num = 3

  def is_prime(n):
    sq = floor(sqrt(n))
    for p in primes:
      if n % p == 0 and n/p != 1:
        return False
      elif p > sq:
        break
    return True

  while True:
    primes.append(num)
    yield num
    num += 2
    while not is_prime(num):
      num += 2

def is_abundant(n):
  return sum(get_factors(n)) > 2*n

def gen_abundant():
  n = 1
  while True:
    if is_abundant(n):
      yield n
    n += 1

"""
We don't really need a prime number generator for factorization.

In fact, factorization could be computed faster without one
since we wouldn't have to check to see if each potential
factor is prime.

If the potential factor isn't prime, we know that it isn't a factor
of the remaining number because we've already divided out
all the prime factors of the potential factor.

TODO: Don't use prime number generator to generate potential factors
"""
def factorize(num):
  orig_num = num
  factors = defaultdict(int)
  primes = gen_primes()
  factor = next(primes)
  while factor <= floor(sqrt(orig_num)) and num != 1:
    if num % factor == 0:
      factors[factor] += 1
      num /= factor
    else:
      factor = next(primes)
  if num != 1:
    factors[num] += 1
  return factors

def get_factors(num):
  factors = set()
  sq = int(floor(sqrt(num)))
  for i in xrange(1,sq+1):
      if num % i == 0:
        factors.add(i)
        factors.add(num/i)
  return factors

def fib_cond(cond, init=(1,2)):
  x_0, x_1 = init
  while cond(x_0):
    yield x_0
    x_0, x_1 = x_1, x_0 + x_1

def fib_cond_plus_one(cond, init=(1,2)):
  x_0, x_1 = init
  while cond(x_0):
    yield x_0
    x_0, x_1 = x_1, x_0 + x_1
  yield x_0


def fib_to(to):
  return fib_cond(lambda x: x < to)

def find_max_triangle_sum(tri):
  """
  We start from the bottom of the triangle and work
  our way up. We delete the last row and replace the
  second to last row with the maximum total from the position
  in the second to last row to the last.
  i.e.
  We replace each instance of
    a
   b c

  with
   a + max(b,c)
  """
  # TODO Check if triangle is a valid triangle
  while len(tri) > 1:
    # pprint(tri)
    for i, num in enumerate(tri[-2]):
      tri[-2][i] = tri[-2][i] + max(tri[-1][i], tri[-1][i+1])
    del tri[-1]
  return tri[0][0]


