def is_palindrome(num):
    return str(num) == str(num)[::-1]

max_palindrome = 0
for i in xrange(999, 99, -1):
    for j in xrange(i, 99, -1):
        prod = i*j
        if prod < max_palindrome:
            break
        if is_palindrome(prod) and prod > max_palindrome:
            max_palindrome = prod

print max_palindrome
