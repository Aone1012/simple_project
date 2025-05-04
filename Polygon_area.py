from math import tan, pi


def Polygon_area(side, size):
    if side < 3:
        raise ValueError("A polygon must have at least 3 sides.")
    if size <= 0:
        raise ValueError("Side length must be positive.")
    return (side * (size ** 2)) / (4 * tan(pi / side))


# print(Polygon_area())
try:
    side = int(input("Input the number of side: "))
    size = float(input("Input the size of side: "))
    area = Polygon_area(side, size)
    print(area)
except ValueError as e:
    print("Error", e)
