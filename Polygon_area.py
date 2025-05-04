from math import tan,pi


def Polygon_area():
    while True:
        try:
            side = int(input("Input the number of side: "))
            size = float(input("Input the size of side: "))
            Area = ( side *(size**2)) / (4 * tan(pi/side))
            return Area
        except ValueError:
            print("Input the correct Value")
print(Polygon_area())