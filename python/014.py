def get_collatz_len(n):
  l = 1
  while n != 1:
    if n % 2 == 1:
      n = 3*n + 1
    else:
      n /= 2
    l += 1
  return l

m = 0
num = 0
for i in xrange(1, 1000000):
  l = get_collatz_len(i)
  if l >= m:
    m = l
    num = i

print m, num
