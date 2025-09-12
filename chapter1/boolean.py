is_boiling = True
total_count = 9
print(f"value of {is_boiling}")
stri_count = total_count + is_boiling #upcasting = converted one data type into another here boolean automatically get  converted into number
print(f"total Actions: {stri_count}")
milk_present = 2# no milk present 
print(f"Is there milk ? {bool(milk_present)}")

# AND :- both should be true 
# OR :- Any one can be true

water_hot = True
tea_added = True #False

can_server = water_hot and tea_added
print(f"Can Serve chai ?? {can_server}")
