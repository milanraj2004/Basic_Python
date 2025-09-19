
names = ["Alice", "Bob", "Charlie"]
bills = [78,95,55,45]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} dollars")  