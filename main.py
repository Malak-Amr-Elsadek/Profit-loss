buying_price=int(input("Enter buying price:"))
selling_price=int(input("Enter selling price:"))

if (selling_price>buying_price):
    profit=selling_price-buying_price
    print("proft  is",profit)
else:
    loss=buying_price-selling_price
    print("loss  is",loss)