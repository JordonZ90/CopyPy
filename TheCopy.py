import copy
box = ['A', 'B', 'C', 'D']
print(id(box))

cube = copy.copy(box)
print(id(cube))  # Cube is a different list with different id
cube[1] = 42

print(box)
print(cube)