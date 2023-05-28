def christmas_tree(height):
    for i in range(height):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))


christmas_tree(10)