
cubes = []
def generate_cube(x):
    for i in range(1, x+1):
        cubes.append(i ** 3)
    print(cubes)


def cube_yield(x):
    for i in range(1, x+1):
       yield(i ** 3)

print(cube_yield(10))