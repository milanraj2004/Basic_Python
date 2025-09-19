
flavours =  ["Ginger", "Out Of Stock", "Lemon Tea", "Discontinued","Tulsii" ]


for flavour in flavours:
    if flavour == "Out Of Stock":
        continue
    if flavour == "Discontinued":
        print(f"{flavour} item found")
        break
    print(f"{flavour} item found")

print(f"Outside  of Loop ")