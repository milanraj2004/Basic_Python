order_amount = int(input("Enter the Order Amount:-- "))

delivery_fees = 0 if order_amount > 300 else 30

print(f"Delivery fees is {delivery_fees}")