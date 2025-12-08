chai_type = "Plain"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Iranian"
    kitchen()


front_desk()
print("final chai_type:", chai_type)