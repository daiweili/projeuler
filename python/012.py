from projeuler.math.integer import get_factors

def gen_triangular_numbers():
  n = 1
  while True:
    yield n * (n+1) / 2
    n += 1

triangular_numbers = gen_triangular_numbers()
n = next(triangular_numbers)

while len(get_factors(n)) < 500:
  n = next(triangular_numbers)

print n
