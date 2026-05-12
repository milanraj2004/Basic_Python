def make_tea():
   # return "Here is Masala Tea"
   print("here is Your tea")

print(make_tea())

returnValue = make_tea()
print(returnValue)

def idle_chaiWala():
   pass

print(idle_chaiWala())

def sold_cups():
   return 120

total = sold_cups()
print(total)

def chai_status(cups_left):
   if cups_left ==0:
      return "Chai is REady"
   
print(chai_status(0))
print(chai_status(200))



def chaiReport():
   return 1000,205
sold , remaining = chaiReport()
print("sold",sold)
print("report",remaining)