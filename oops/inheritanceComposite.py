class BaseChai:
    def __init__(self, name):
        self.name = name

    def make_chai(self):
        print(f"Making {self.name} chai")


class MasalaChai(BaseChai):
    def add_spices(self):
        print(f"Adding Cardaomom and Ginger to {self.name} chai")


class ChaiShop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")
    def serve(self):
        print(f"Serving {self.chai.name} chai In chai shop")
        self.chai.make_chai()

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai

   

shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()
    
