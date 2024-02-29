grocery_items = [

    ("Apples", 99),
    ("Bananas", 49),
    ("Milk", 29),
    ("Eggs", 99),
    ("Bread", 49),
    ("Cheese", 99),
    ("Tomatoes", 79),
    ("Almonds", 99),
    ("Orange Juice", 49),
    ("Rice", 99),
    ("Pasta", 49),
    ("Green Peas", 99),
    ("Yogurt", 29),
    ("Coffee", 49),

]

t=0

for item_price in grocery_items:
    t += item_price[1]

print (t)

