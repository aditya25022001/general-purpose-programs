args = [3,6]
print(list(range(*args)))
def make_incrementor(n):
     return lambda x: x + n

f = make_incrementor(42)
l = []
for y in range(10):
    l.append(f(y))
print(l)
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)