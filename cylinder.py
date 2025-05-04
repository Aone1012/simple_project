"""
def Calculate_Zylinder_Area():
    Radius = input("Input the Radius of Cylinder: ")
    Height = input("Input the Height of Cylinder: ")
    pi = 22.7
    if Radius.isdigit() and Height.isdigit() :
        print(f"Volume of Cylinder: {(float(Radius)**2)*float(Height)*pi} ")
        print(f"Volume of all Area : {2*pi*(float(Radius)**2)+float(Height)*2*pi} ")


    else:
        print("Bitte geben Sie eine Zahl ein : ")
        return Calculate_Zylinder_Area()

Calculate_Zylinder_Area()
"""
from math import pi
def Calculate_Cylander_Area():
    while True:
        try:
            Radius = float(input("Input the Radius: "))
            break
        except ValueError:
            print("Invalid input, Please input an number: ")

    while True:
        try:
            Height = float(input("Input the Height: "))
            break
        except ValueError:
            print("Invalid input, Please input an number: ")


    Volume = (Radius**2)*(Height*pi)
    Surface_Area = 2*pi*Radius*Height+(Height**2*2*pi)

    print(f"Volume is:{Volume} ")
    print(f"Surface Area is:{Surface_Area} ")

Calculate_Cylander_Area()