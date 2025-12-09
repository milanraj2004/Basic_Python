chai = "Ginger chai"

def prepare_chai(order):

    print("Preparing:", order)

prepare_chai(chai)



chai = [1,2,3]
def edit_chai(cup):
    cup[1] = 42 
edit_chai(chai)
print("Edited chai:", chai)
    

def make_chai(tea,milk,sugar):
        print(f"Making chai with {tea}, {milk}, {sugar}")
        print(tea,milk,sugar)

make_chai("Darjelling","yes","Low") #positional arguments

make_chai(tea="Darjelling",sugar="Low",milk="yes") #keyword arguments)