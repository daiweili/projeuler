def get_nlen_substr(s, n):
  """
  Get all length n substrings from s
  """
  iters = []
  for i in xrange(n):
    iters.append(iter(s[i:]))
  while True:
    try:
      yield ''.join([next(i) for i in iters])
    except StopIteration:
      break

ONES = { 1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine'
        }

TWENTIES = {
        2:'twenty',
        3:'thirty',
        4:'forty',
        5:'fifty',
        6:'sixty',
        7:'seventy',
        8:'eighty',
        9:'ninety',
        }

TENS = {
        10:'ten',
        11:'eleven',
        12:'twelve',
        13:'thirteen',
        14:'fourteen',
        15:'fifteen',
        16:'sixteen',
        17:'seventeen',
        18:'eighteen',
        19:'nineteen',
        }

BIG = ['million', 'billion', 'trillion', 'quadrillion']


def int_to_eng(num):
  def sub_hundred_to_eng(num):
    assert(num < 100)
    if num in TENS.keys():
      return TENS[num]
    elif num < 10:
      return ONES[num]
    else:
      partial = TWENTIES[num/10]
      if num % 10 != 0:
        partial += ' %s' % ONES[num % 10]
      return partial
  def sub_thousand_to_eng(num):
    assert(num >= 100 and num < 1000)
    partial = ONES[num/100] + ' hundred'
    rem = num - num/100*100
    if rem > 0:
      partial += ' and ' + sub_hundred_to_eng(rem)
    return partial
  def sub_ten_thousand_to_eng(num):
    assert(num >= 1000 and num < 10000)
    partial = ONES[num/1000] + ' thousand'
    rem = num - num/1000*1000
    if rem >= 100:
      partial += ' ' + sub_thousand_to_eng(rem)
    elif rem > 0:
      partial += ' and ' + sub_hundred_to_eng(rem)
    return partial

  if num < 100:
    return sub_hundred_to_eng(num)
  elif num < 1000:
    return sub_thousand_to_eng(num)
  elif num < 10000:
    return sub_ten_thousand_to_eng(num)
  else:
    raise NotImplemented

def test_single_digit():
  assert int_to_eng(5) == 'five'

def test_ten():
  assert int_to_eng(10) == 'ten'

def test_teen():
  assert int_to_eng(14) == 'fourteen'

def test_two_digit():
  assert int_to_eng(37) == 'thirty seven'

def test_three_digit():
  assert int_to_eng(243) == 'two hundred and forty three'
  assert int_to_eng(105) == 'one hundred and five'
  assert int_to_eng(500) == 'five hundred'

def test_four_digit():
  assert int_to_eng(5764) == 'five thousand seven hundred and sixty four'
  assert int_to_eng(9211) == 'nine thousand two hundred and eleven'
  assert int_to_eng(1045) == 'one thousand and forty five'
  assert int_to_eng(3000) == 'three thousand'


