total = 0
item_count = int(input("Pick a number "))
for item in range(item_count):
    item_price = int(input("Enter price: "))
    total += item_price
print(total)