class CoffeeCup:
    size = 150 #ml

    def describe(self):
       
       return f"A {self.size} ml cup of coffee"
    

cup = CoffeeCup()
print(cup.describe())
print(CoffeeCup.describe(cup))

cup_two = CoffeeCup()
cup_two.size = 200
print(CoffeeCup.describe(cup_two))