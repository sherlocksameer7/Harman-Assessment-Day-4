num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square = list(map(lambda a: a ** 2, num_list))
cube = list(map(lambda b : b ** 3, num_list))
print(sorted(square))
print(sorted(cube))