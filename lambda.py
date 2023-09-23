# double = lambda x: x * 2
# print(double(5))

# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)

points = [(2, 5), (1, 3), (4, 1), (7, 6)]
sorted_points = sorted(points, key=lambda x: x[1])
print(sorted_points) 

'''def add(a, b):
    return a + b

    add = lambda a, b: a + b
'''