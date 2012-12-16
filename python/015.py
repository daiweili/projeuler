from math import factorial
from operator import mul

"""
The answer should be 40 choose 20.
Once you recognize that this is Pascal's
triangle turned sideways, getting the analytical
answer is easy
"""
print reduce(mul, xrange(21, 41)) / factorial(20)
