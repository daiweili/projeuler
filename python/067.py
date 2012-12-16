from projeuler.math.integer import find_max_triangle_sum
import requests
import string

r = requests.get('http://projecteuler.net/project/triangle.txt')
triangle = r.content
triangle = map(string.split, triangle.strip().split('\n'))
triangle = [map(int, row) for row in triangle]

print find_max_triangle_sum(triangle)
