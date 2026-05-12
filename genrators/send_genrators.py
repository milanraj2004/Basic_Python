def chai_customer():
    print("WelCome to the Chai Shop!    What would you like to order?")
    order = yield
    while True:
        print(f"Your order is {order}.    Please wait while we prepare your chai.")
        # order = yield // Wait for the next order
        order = yield  # Wait for the next order 

stall = chai_customer()
next(stall)  # Start the generator
stall.send("Masala Chai")
stall.send("Ginger Chai")
stall.send("Cardamom Chai")
