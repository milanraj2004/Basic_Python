class Chai:
    tempreature = "hot"
    strength = "strong"
    sweetener = "sugar"



cutting = Chai()

print(cutting.tempreature)
print(cutting.strength)
print(cutting.sweetener)

cutting.tempreature = "cold"
cutting.cup = "glass"
print(cutting.tempreature)
print(Chai.tempreature)


del cutting.tempreature
del cutting.cup
print(cutting.tempreature)

print(cutting.cup)