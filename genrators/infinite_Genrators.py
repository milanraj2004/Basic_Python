
def infinite_chai():
    count = 1
    while True:
        yield f"Refill Chai {count}"
        count += 1
# Example usage:

refill = infinite_chai()
user2 = infinite_chai()
for _ in range(3):
    print(next(refill))
# Output:
# Refill Chai 1
# Refill Chai 2
# Refill Chai 3

for _ in range(6):
    print(next(user2))
    