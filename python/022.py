import requests

r = requests.get('http://projecteuler.net/project/names.txt')
names = r.content.replace('\"', '').split(',')
names.sort()
print names
print sum([(i+1)*sum(map(lambda c: ord(c) - ord('A') + 1, name)) for i, name in enumerate(names)])
