sugar = 2
print(f"Initial Sugar: {sugar}")

sugar = 18
print(f"Initial Sugar: {sugar}")

print(f"id of two is : {id(2)}")
print(f"id of 12 is :  {id(12)}")

spice_name = set()
print(f"inital print spice mix id{id(spice_name)}")
print(f"After print spice mix id{spice_name}")
spice_name.add("Ginger/ Adrakh")
spice_name.add("Elaichi/ Cardamom")
print(f"After print spice mix id{id(spice_name)}")
print(f"After print spice mix name  {spice_name}")
