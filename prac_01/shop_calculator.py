number_of_item = int(input("Enter the number of items: "))
total = 0
for i in range(0, number_of_item):
    price_of_item = float(input("Enter the price of item: "))
    total += price_of_item
if total > 100:
    discount = total * 0.1
    total = total - discount
print(f"Total price for {number_of_item} is{total: .2f}.")

