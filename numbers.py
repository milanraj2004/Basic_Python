#integer
black_tea_grams = 14
ginger_grams = 3
total_grams = black_tea_grams + ginger_grams
print(f"total grams of base tea is {total_grams}")
remaning_tea = black_tea_grams -ginger_grams
print(f"total grams of base tea is {remaning_tea}")

milk_litres = 7
servings = 4
milk_serving = milk_litres/servings
print(f"Milk serving {milk_serving}")

total_tea_bags = 7
pots = 4 
bags_per_pot = total_tea_bags // pots
print(f"bags are {bags_per_pot}")

total_pots = 10
pots_per = 3
leftover_pods = total_pots % pots_per

print(f"total Left Over Pods are {leftover_pods}")

base_flavor = 2
scale_Factor = 3
powerful_flavor = base_flavor ** scale_Factor
print(f"powerful scaled strength {powerful_flavor}")

total_tea_harvested = 1_000_000_000
# we can write like this; Python ignores underscores for better readability
print(f"tea leaves : {total_tea_harvested}")