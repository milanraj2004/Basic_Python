chai_order = dict(type="Masala Chai", size="Large", sugar=20)
print(f"chai Order: {chai_order}")

chai_recipe = {}

chai_recipe["base"] ="Masala Chai"
chai_recipe["liquid"] = "milk"

#print(f"chai orderred: {chai_order['base']}")
#print(f"chai items liquid are: {chai_order['liquid']}")

#del chai_order["liquid"]

print(f"chai items liquid are: {chai_order}")

print(f"Is Sugar in the Order ?? {'sugar' in chai_order}")

chai_order = {"type":"gingerchai","size":"Med","sugar":2}

# print(f"Order Details (keys):{chai_order.keys()}")
# print(f"Order Details (keys):{chai_order.values()}")
# print(f"Order Details (keys):{chai_order.values()}")

last_item = chai_order.popitem()

print(f"Removed last item : {last_item}")

extra_spices = {"cardamom":"crushed","ginger":"sliced"}

chai_recipe.update(extra_spices)

print(f"Updated Chai Recipie {chai_recipe}")

chai_size = chai_order["size"]

print(f"updated chai size is {chai_size}")

customer_note = chai_order.get("note","NO Note")
print(f"customer_note is {customer_note}")