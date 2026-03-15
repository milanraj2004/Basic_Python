def pure_chai(cups):
    return cups * 20
total_tea = 0
# pure functions and impure functions

def impure_chai(cups):
    global total_tea
    total_tea += cups

def pour_chai(n):
    print(f"Pouring chai, {n} cups left")
    if n == 0:
        return "No chai to pour"
    return pour_chai(n-1)

print(pour_chai(5))



chai_types = ["Masala", "Adrak", "Elaichi","Masala"]

set_chai = list(filter(lambda chai : chai != "Masala", chai_types   ))
print(set_chai)