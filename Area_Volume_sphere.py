from math import pi
def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value>0 :
                return value
            else:
                print("Please Enter a Positive Number")
        except ValueError:
            print("Please Enter an correct Value")
def sphere():
    Radius = get_positive_number("Please input the Radius: ")

    Sur_Area = 4 * pi * Radius**2
    Volume =  (4/3)* pi * (Radius**3)
    print(f"Surface Area is: {Sur_Area:}\nVolume is: {Volume: .2f} ")

sphere()