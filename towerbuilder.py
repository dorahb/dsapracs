def tower_builder(n_floors):
    # build here
    return [('*' * (2 * i + 1)).center(2 * n_floors - 1) for i in range(n_floors)]


print(tower_builder(10))