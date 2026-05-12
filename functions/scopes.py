def serve_chai():
    chai_type = "Masala Chai"
    print(f"Inside function: Serving {chai_type}")
    print(f"Inside function: Serving {chai_type}")

    # git conflict marker test


chai_type = "Ginger Chai"
serve_chai()
print(f"Outside function: Serving {chai_type}")

def chai_counter():
    chai_order = "Lemon Chai"
    def print_order():
        chai_order = "Cardamom Chai"
        print(f"Inside nested function: Serving {chai_order}")
    print(f"Outside nested function: Serving {chai_order}")
    print_order()
    print(f"After nested function: Serving {chai_order}")
chai_order = "Tulsi Chai"
chai_counter()
print(f"Global scope: Serving {chai_order}")
