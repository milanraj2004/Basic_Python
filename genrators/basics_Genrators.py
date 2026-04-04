def serveTea():
    yield 'Tea'
    yield 'Coffee'
    yield 'Milk'

stalls = serveTea()

for item in stalls:
    print(item)

def getTeaList():
    return ['Tea', 'Coffee', 'Milk']
# genrator function

def get_chai_get():
    yield 'Tea'
    yield 'Coffee'
    yield 'Milk'

chai = get_chai_get()
print(chai)
print(next(chai))
print(next(chai))
print(next(chai))
print(next(chai)) # StopIteration error