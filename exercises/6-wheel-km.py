import math

# Exercise 6

diameter = float(50)

circunference = (diameter*math.pi)

distancecm = circunference / 100000

distancekm = round(1/distancecm)

print(f"The turns are: {distancekm})