"""
def calculate_area():
    Gaedeh = input("Input the Gaedeh: ")
    Height  = input("Input the Height: ")
    if Gaedeh.isdecimal() and Height.isdecimal() :
        return print(f"The Area : {float(Gaedeh) * float(Height)}")
    else:
        print("Nummer,bitte!!")
        calculate_area()


calculate_area()
Wrong
"""
def calculate_area():
    while True:
        try:
            Gaedeh = float(input("Input the Gaedeh: "))
            break
        except ValueError:
            print("Invalid input, Please input an number: ")
    while True:
        try:
            Height  = float(input("Input the Height: "))
            break
        except ValueError:
             print("Invalid input, Please input an number: ")
    Area = Gaedeh * Height

    print(f"The Area :{Area}")


calculate_area()

