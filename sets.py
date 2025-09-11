essential_spices = {"cardamom","ginger","cinnamon"}
optional_spices = {"cloves","ginger","blackpepper"}

all_spices = essential_spices | optional_spices

print(f"All Spices : {all_spices}")

common_spices = essential_spices & optional_spices

print(f"Common Spices {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"Only Essentials are : {only_in_essential}")

# membership test 

print(f"Is this cloves  in essential spices {'cloves'in essential_spices}")