#List :- It is mutable 
 
ingredients = ["water","milk", "tealeaves"]
ingredients.append("sugar")

print(f"Ingredients are {ingredients}")

ingredients.remove("water")
print(f"Ingredients are {ingredients}")

spice_options = ["ginger","cardamom"]

chai_ingridents = ["water","milk"]

chai_ingridents.extend(spice_options)
print(f"chai: {chai_ingridents}")
chai_ingridents.insert(2,"sugar")
print(f"chai: {chai_ingridents}")

last_added = chai_ingridents.pop()
print(f"chai Added: {last_added}")
chai_ingridents.reverse()
print(f"chai: {chai_ingridents}")

chai_ingridents.sort()
print(f"chai: {chai_ingridents}")


sugar_levels = [1,2,3,4,5,6]

print(f"MAximum Sugar Level : {max(sugar_levels)}")

print(f"Minimum Sugar Level : {min(sugar_levels)}")


# Operator Overloading 

base_liquid = ["water","Milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor

print(f"Liquid Mix {full_liquid_mix}")

strong_brew = ["black tea, Green Tea"] *3

print(f"string brew : {strong_brew}")


raw_spices = bytearray(b"CINNAMON")
raw_spices = raw_spices.replace(b"CINNA",b"CARD")
print(f"Bytes : {raw_spices}")

