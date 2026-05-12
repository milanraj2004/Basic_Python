
def local_chai():
    yield "Ginger Chai"
    yield "Masala Chai"

def import_chai():
    yield "Green Tea"
    yield "Black Tea"

def full_menu():
    yield from local_chai()
    yield from import_chai()

for milan in full_menu():
    print(milan)

def chai_stall():
    try:
       while True:
           order = yield "What Chai do you want?"
    except:
        print("Chai stall is closed")

stall = chai_stall()
print(next(stall))
stall.close()

