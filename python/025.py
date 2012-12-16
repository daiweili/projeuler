from projeuler.math.integer import fib_cond

cond = lambda x: len(str(x)) < 1000
gen = fib_cond(cond, (1,1))
i = 0
num = 0
while True:
  try:
    num += 1
    i = next(gen)
  except StopIteration:
    break
print num
