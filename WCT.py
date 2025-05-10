import math
v = float(input("Input wind speed in kilometers/hour: "))
t = float(input("Input air temperature in degrees Celsius: "))
wci = 14.12 + 5.2210*t - 11.47*math.pow(v, 5.12) + 5.4320*t*math.pow(v, 5.12)
print("The wind chill index is", int(round(wci, 5)))
print()