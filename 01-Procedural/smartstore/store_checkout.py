
print("Welcome to the Smart Store!")
print("1. Notebook - 70 AFN")
print("2. Pen Pack - 40 AFN")
print("3. USB Flash Drive - 250 AFN")

product = int(input("What product do you want?"))
price = 0
if product == 1:
    price = 70
elif product == 2:
    price = 40
elif product == 3:
    price = 250

quantity = int(input("What quantity do you want?"))
subtotal = quantity * price