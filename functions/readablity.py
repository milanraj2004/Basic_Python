
def calculateBill(cups, pricePerCup):
    return cups * pricePerCup

myBill = calculateBill(3, 25)
print("My bill is: $" + str(myBill))

print(myBill)

print("My bill is: $" + str(calculateBill(3, 25)))