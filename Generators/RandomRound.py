def square(n):
    yield n * n

def cube(n):
    yield n * n * n

for i in square(65):
    print(f"Square: {i}")

for i in cube(65):
    print(f"Cube: {i}")


##List Comprehension

lc = (a*a*a for a in range(10))
print(lc.__next__())
print(lc.__next__())
print(lc.__next__())
print(lc.__next__())

