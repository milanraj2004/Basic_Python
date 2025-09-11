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
