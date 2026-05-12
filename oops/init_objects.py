class ChaiOrder: 
    def __init__(self,type_,size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size} ml of {self.type} chai "
        
order_one = ChaiOrder("Masala", 200)
print(order_one.summary())

order_two = ChaiOrder("Ginger", 150)
print(order_two.summary())
