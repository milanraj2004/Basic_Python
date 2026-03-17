menu = [
    "Grilled Chicken Breast Food",
    "Beef Stir-Fry Food",
    "Shrimp Scampi Food",
    "Pork Chops with Apples Food",
    "Lamb Kebabs Food",
    "Fish Tacos Food",
    "Turkey Meatballs Food",
    "Salmon with Dill Sauce Food",
    "BBQ Ribs ",
    "Chicken Alfredo Pasta Food",
    "Grilled Vegetable Skewers Food",
    "Caprese Salad Food",
    "Veggie Stir-Fry Food",
]

# BBQ_Ribs = [food for food in menu if "Food" in food]
# print(BBQ_Ribs)

milan = [food for food in menu if len(food) > 20]
print(milan)