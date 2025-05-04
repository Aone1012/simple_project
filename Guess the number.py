import random
from random import randint


def Zahlenratespiel():
    Random_value = randint(1,100)
    while True:
        try:
            guess_value = int(input("Guess your Value: "))
            if guess_value > Random_value:
                print("Guess lower Number")
            elif guess_value < Random_value:
                print("Guess Higher")
            else:
                print("Super , Right Number")
                break
        except ValueError:
            print("Wrong Value (Falscher Wert)")

Zahlenratespiel("Enter Your Guess (Geben Sie Ihre Vermutung ein) : ")


def Zahlenratespiel_Coumpter():
    a =1
    b =99
    Guess = randint(a,b)
    print(Guess)
    My_Nummer = input("OK? ")

    while A != My_Nummer  :
        if My_Nummer == 'H':
            a = Guess
            Guess = randint(a,b)
            print(Guess)
            My_Nummer = input("OK? ")

        elif My_Nummer =='L':
            b = Guess
            Guess = randint(a,b)
            print(Guess)
            My_Nummer = input("OK? ")
        else:
            print("Wrong Value")
            My_Nummer = input("OK? ")

    print("Yes Computer you did it")


Zahlenratespiel_Coumpter()

