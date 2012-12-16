# Naive calculation
print abs(sum(xrange(101))**2 - sum(map(lambda x: x**2, xrange(101))))
"""
Smarter way to do it on paper:
    1 + 2 + 3 + ... + n = n * (n+1) / 2
    (n * (n+1) / 2)^2 = n^2 * (n+1)^2 / 4

    1^2 + 2^2 + 3^2 + ... + n^2 = n * (n+1) * (2n+1) / 6
"""
