import math

formatPI = "value of PI: {:.5f}".format(math.pi)
print(formatPI)
radius = float(input("Enter the radius"))
areaCircle = math.pi * radius ** 2
print(f"Are of circle areaCircle {areaCircle:.4f}")
