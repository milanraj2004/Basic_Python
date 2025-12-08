def update_order():
    chai_type = "Elaichi"


    def kitchen():
        #nonlocal chai_type
        chai_type = "Adrak Elaichi"
        print(f"Inside kitchen: {chai_type}")
    kitchen()
    print(f"Outside kitchen: {chai_type}")
    print("After Kitchen update", chai_type)
update_order()