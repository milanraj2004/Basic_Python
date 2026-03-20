
favourite_chais  = ["Masala Chai","GreenTea","Lemon Tea","Ginger Tea","Masala Chai"]

unique_chai = {chai for chai in favourite_chais if len(chai) < 8}
print(unique_chai)

recipes = {
    "Masala Chai": ["Tea Leaves", "Milk", "Sugar", "Spices"],
    "Green Tea": ["Green Tea Leaves", "Water"],
    "Lemon Tea": ["Tea Leaves", "Water", "Lemon"],
    "Ginger Tea": ["Tea Leaves", "Water", "Ginger"],
}

unique_ingredients = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_ingredients)