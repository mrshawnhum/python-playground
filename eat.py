def create_cubes(n):
    result = []
    for x in range(n):
        yield x**3

for x in create_cubes(10):
    print(x)

def gen_fibon(n):

    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

for num in gen_fibon(10):
    print(num)

def simple_gen():
    for x in range(3):
        yield x

for num in simple_gen():
    print (num)

g = simple_gen()

print(next(g))