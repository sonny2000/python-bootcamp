

#for item in range(100):
#   if 20 <= item <= 80:
#      continue
 #  print(item)


total = 0
item_count = int(input("Enter number of items: "))
for item in range (item_count):
    item_price = int(input("Enter price: "))
    total += item_price
print (total)
