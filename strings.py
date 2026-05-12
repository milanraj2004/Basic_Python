# Strings are Immutable 
chai_type = "Ginger chai"
customer_name = "Milan Raj"

print(f"Order for {customer_name}: {chai_type} Please !!")


chai_Description = "Aromatic And Bold Chai Strong"
print(f"first Word : {chai_Description [0:8]}")
print(f"first Word : {chai_Description [0:8:2]}") # from start and mid and step where the step cut that words 
print(f"first Word : {chai_Description [12:]}") # fromm where the data from index to the last 
print(f"first Word : {chai_Description [::-1]}") # for reversing 


label_text = "Chai Special"
ecoded_label = label_text.encode("utf-16")
print(f" Label {label_text}")
print(f"Encoded Label {ecoded_label}")
decoded_label = ecoded_label.decode("utf-16")
print(f"Decoded Label: {decoded_label}")
