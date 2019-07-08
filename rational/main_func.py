from rational_func import rational, rational_add, rational_str as s

half = rational(1, 2)
third = rational(1, 3)

total = rational_add(half, third)

print(f"{s(half)} + {s(third)} = {s(total)}")
