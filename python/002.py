from projeuler.math.integer import fib_to

print sum(filter(lambda x: x % 2 == 0, fib_to(4000000)))
