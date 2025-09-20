
staff =  [("Amit", 16), ("Milan", 20), ("Raja Babu", 23),]

for name, age in staff:
    if age >= 18:
        print(f"{name}  is Eligble for training")
        break
else:
    print("No one is eligble for training")