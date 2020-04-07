# read length of the legs of a right triangle
leg1 = float(input())
leg2 = float(input())

# compute length of hypotenuse
hypotenuse = (leg1 ** 2 + leg2 ** 2) ** 0.5

# print length of hypotenuse
print(f'Length of the hypotenuse: {hypotenuse:.3f}')
