from collections import Counter
from collections import defaultdict
from collections import namedtuple

mylist = [1, 1, 1, 2, 2, 3, 2]

# print(Counter(mylist))

d = {'a':10}
print(d)

d = defaultdict(lambda: 0)
d['correct'] = 100
print(d['correct'])

Dog = namedtuple('Dog', ['age', 'breed', 'name'])
sammy = Dog(age=5, breed='Husky', name='Same')
print(sammy)